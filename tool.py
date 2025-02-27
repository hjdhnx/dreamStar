#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : tool.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2025/2/27

import webview
import threading
import pygetwindow as gw
import win32gui
import time
from utils.autogui import Screen, Mouse, KeyBoard, Message
from config import Config

game_config = Config()
keybord = KeyBoard()
mouse = Mouse()
screen = Screen()
message = Message()


class ToolController:
    def __init__(self):
        self.config = game_config
        self.game_url = "https://gamer.qq.com/v2/game/96897"
        self.game_window = None
        self.access_code = self.config.access_code
        self.game_title = self.config.game_title
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def create_control_window(self, js_api):
        """创建控制面板窗口"""
        html = """
        <style>
            .control-panel { padding:20px; background:#f5f5f5; }
            button { display:block; width:100%; margin:10px 0; padding:15px; }
        </style>
        <div class="control-panel">
            <button onclick="pywebview.api.operate()">操作（空格）</button>
            <button onclick="pywebview.api.move_left()">向左移动（A键）</button>
            <button onclick="pywebview.api.move_right()">向右移动（D键）</button>
            <button onclick="pywebview.api.move_up()">向上移动（W键）</button>
            <button onclick="pywebview.api.move_down()">向下移动（S键）</button>
            <button onclick="pywebview.api.fly()">弹射飞行（Q键）</button>
            <button onclick="pywebview.api.jump()">跳跃（SHIFT键）</button>
            <button onclick="pywebview.api.reset_postion()">重置位置（R键）</button>
            <p>脚本启动时间: $start_time</p>
        </div>
        """.replace('$start_time', self.start_time)

        self.control_window = webview.create_window(
            '元梦农场控制台',
            html=html,
            width=300,
            height=720,
            confirm_close=True,
            js_api=js_api,
            resizable=False,  # 控制台窗口不可调整大小
            # frameless=True,   # 去除边框
        )

    def init_position(self):
        time.sleep(1)
        self.update_control_window_position()

    def update_control_window_position(self):
        """更新控制台窗口的位置，使其紧贴游戏窗口右侧"""
        try:
            windows = gw.getWindowsWithTitle(self.game_title)
            if windows:
                game_window = windows[0]
                # 获取游戏窗口的当前坐标和尺寸
                game_x, game_y = game_window.left, game_window.top
                game_width, game_height = game_window.width, game_window.height

                # 设置控制台窗口紧贴游戏窗口右边
                self.control_window.move(game_x + game_width - 10, game_y)
        except Exception as e:
            print(f"获取游戏窗口位置失败: {e}")

    def listen_window_move(self):
        """监听游戏窗口移动事件"""

        def enum_window_callback(hwnd, lParam):
            # 获取窗口标题
            title = win32gui.GetWindowText(hwnd)
            if title == self.game_title:
                # 获取窗口的位置信息
                rect = win32gui.GetWindowRect(hwnd)
                x, y, _, _ = rect
                # 如果窗口位置发生变化，则更新控制台窗口位置
                if hasattr(self, 'last_position') and self.last_position != (x, y):
                    print(f"游戏窗口位置变化: {x}, {y}")
                    self.update_control_window_position()
                self.last_position = (x, y)

        # 注册窗口枚举回调函数
        win32gui.EnumWindows(enum_window_callback, None)

    def run(self):
        """启动监听并定时更新控制台窗口位置"""
        while True:
            self.listen_window_move()
            time.sleep(0.02)  # 每秒更新一次


class GameApi():
    def log(self, value):
        print(value)

    def click(self, key='space'):
        self._activate_game_window()
        keybord.press(key)

    def press(self, key, seconds):
        self._activate_game_window()
        keybord.keyDown(key)
        threading.Timer(seconds, keybord.keyUp, args=[key]).start()

    def operate(self):
        """操作,浇水助产等"""
        self.click('space')

    def move_left(self):
        """左移操作"""
        self.press('a', 1.0)

    def move_right(self):
        """右移操作"""
        self.press('d', 1.0)

    def move_up(self):
        """上移操作"""
        self.press('w', 1.0)

    def move_down(self):
        """下移操作"""
        self.press('s', 1.0)

    def fly(self):
        """弹射飞行"""
        self.click('q')

    def jump(self):
        """跳跃"""
        self.click('shift')

    def reset_postion(self):
        """重置位置操作"""
        self.click('r')

    def _activate_game_window(self):
        """激活游戏窗口"""
        try:
            windows = gw.getWindowsWithTitle(game_config.game_title)
            print('windows:', windows)
            if windows:
                windows[0].activate()
        except Exception as e:
            print(f"窗口激活失败: {e}")


if __name__ == '__main__':
    toolC = ToolController()
    api = GameApi()

    toolC.create_control_window(api)
    # 启动一个线程，不断监听窗口移动事件并更新控制台窗口位置
    threading.Thread(target=toolC.init_position, daemon=True).start()
    threading.Thread(target=toolC.run, daemon=True).start()

    # 启动主界面
    webview.start()

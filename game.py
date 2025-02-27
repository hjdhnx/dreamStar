#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : game.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2025/2/27

import webview
import pygetwindow as gw
from config import Config
game_config = Config()


class GameController:
    def __init__(self):
        self.config = game_config
        self.game_url = "https://gamer.qq.com/v2/game/96897"
        self.game_window = None
        self.access_code = self.config.access_code
        self.game_title = self.config.game_title

    def create_game_window(self):
        """创建游戏主窗口"""
        self.game_window = webview.create_window(
            self.game_title,
            url=self.game_url,
            width=1280,
            height=720,
            confirm_close=True,
            resizable=False,  # 禁用窗口调整大小
            # frameless=True,   # 可选，去除边框
        )

    def _activate_game_window(self):
        """激活游戏窗口"""
        try:
            windows = gw.getWindowsWithTitle(self.game_title)
            print('windows:', windows)
            if windows:
                windows[0].activate()
        except Exception as e:
            print(f"窗口激活失败: {e}")


if __name__ == '__main__':
    gameC = GameController()
    gameC.create_game_window()
    # 启动主界面
    webview.start()

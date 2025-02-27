#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : autogui.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2025/2/27

import pyautogui, sys


class Screen:
    def size(self):
        """
        获取屏幕尺寸
        :return: (1920, 1080)
        """
        return pyautogui.size()

    def onScreen(self, x, y):
        """
        判断是否在屏幕上
        :param x:
        :param y:
        :return: true/false
        """
        return pyautogui.onScreen(x, y)

    def screenshot(self, *args):
        return pyautogui.screenshot(*args)

    def locateOnScreen(self, *args):
        return pyautogui.locateOnScreen(*args)

    def locateCenterOnScreen(self, *args):
        return pyautogui.locateCenterOnScreen(*args)

    def locateAllOnScreen(self, *args):
        return pyautogui.locateAllOnScreen(*args)

    def pixel(self, *args):
        return pyautogui.pixel(*args)

    def pixelMatchesColor(self, *args):
        return pyautogui.pixelMatchesColor(*args)

    def center(self, *args):
        return pyautogui.center(*args)


class Mouse:
    def position(self):
        """
        获取鼠标当前位置
        :return: (187, 567)
        """
        return pyautogui.position()

    def moveTo(self, x, y, seconds=None):
        """
        鼠标移动到 x,y
        :param x:
        :param y:
        :param seconds: 延迟的秒数
        :return:
        """
        return pyautogui.moveTo(x, y, seconds)

    def move(self, _x, _y):
        """
        鼠标相对移动 _x,y
        :param _x:
        :param _y:
        :return:
        """
        return pyautogui.move(_x, _y)

    def dragTo(self, x, y, button='left'):
        """
        鼠标拖动到x,y
        :param x:
        :param y:
        :param button: left/right/middle
        :return:
        """
        return pyautogui.dragTo(x, y, button)

    def click(self, x=None, y=None, button='left'):
        """
        鼠标单击,不传坐标就点击当前位置，传了就移动并点击给定坐标。用指定的按钮
        :param x:
        :param y:
        :param button: left/right/middle
        :return:
        """
        return pyautogui.click(x, y, button)

    def doubleClick(self, x, y, button='left'):
        """
        鼠标双击,不传坐标就点击当前位置，传了就移动并点击给定坐标。用指定的按钮
        :param x:
        :param y:
        :param button: left/right/middle
        :return:
        """
        return pyautogui.click(x, y, button)

    def mouseDown(self, button='left'):
        """
        鼠标按键按下
        :param button:
        :return:
        """
        return pyautogui.mouseDown(button)

    def mouseUp(self, button='left', x=None, y=None):
        """
        鼠标移动到x,y并弹起释放
        :param button:
        :param x:
        :param y:
        :return:
        """
        return pyautogui.mouseUp(button, x, y)

    def scroll(self, pos, x=None, y=None):
        """
        移动到 x,y 并滚轮上下。正代表上，负数代表下
        :param pos:
        :param x:
        :param y:
        :return:
        """
        return pyautogui.scroll(pos, x, y)

    def hscroll(self, pos):
        """
        横向滚动，负数代表往左，正数往右。仅linux和mac系统有效
        :param pos:
        :return:
        """
        return pyautogui.hscroll(pos)


class KeyBoard:
    KEYBOARD_KEYS = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
                     ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
                     '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
                     'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
                     'browserback', 'browserfavorites', 'browserforward', 'browserhome',
                     'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
                     'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
                     'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
                     'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
                     'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                     'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
                     'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
                     'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
                     'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
                     'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
                     'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
                     'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
                     'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
                     'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
                     'command', 'option', 'optionleft', 'optionright']

    def write(self, text, interval=None):
        """
        键盘发送文本
        :param text 文本:
        :param interval: 延迟秒数，可以是0.1
        :return:
        """
        return pyautogui.write(text, interval)

    def press(self, key, presses=1):
        """
        键盘按下按键
        :param key: ‘left’ | ['left', 'left', 'left']
        :param presses: 按下多次。默认1次
        :return:
        """
        return pyautogui.press(key)

    def keyDown(self, key):
        """
        键盘按住不放
        :param key:
        :return:
        """
        return pyautogui.keyDown(key)

    def keyUp(self, key):
        """
        键盘释放弹起
        :param key:
        :return:
        """
        return pyautogui.keyUp(key)

    def hold(self, *args):
        """
        with pyautogui.hold('shift'):
        pyautogui.press(['left', 'left', 'left'])

        :param args:
        :return:
        """
        return pyautogui.hold(*args)

    def hotkey(self, *args):
        """
        热键同时按下，如 hotkey('ctrl', 'shift', 'esc')
        :param args: 多参数，一个参数一个按键
        :return:
        """
        return pyautogui.hotkey(*args)


class Message:
    def alert(self, text='', title='', button='OK'):
        """
        消息警告窗
        :param text:
        :param title:
        :param button:
        :return:
        """
        return pyautogui.alert(text, title, button)

    def confirm(self, text='', title='', buttons=None):
        """
        确认窗
        :param text:
        :param title:
        :param buttons:
        :return:
        """
        if buttons is None:
            buttons = ['OK', 'Cancel']
        return pyautogui.confirm(text, title, buttons)

    def prompt(self, text='', title='', default=''):
        """
        输入窗
        :param text:
        :param title:
        :param default:
        :return:
        """
        return pyautogui.prompt(text, title, default)

    def password(self, text='', title='', default='', mask='*'):
        """
        密码输入
        :param text:
        :param title:
        :param default:
        :param mask:
        :return:
        """
        return pyautogui.password(text, title, default, mask)

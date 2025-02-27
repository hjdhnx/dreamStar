#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : main.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2025/2/27

from game import *
from tool import *

if __name__ == '__main__':
    gameC = GameController()
    gameC.create_game_window()

    toolC = ToolController()
    api = GameApi()

    toolC.create_control_window(api)
    # 启动一个线程，不断监听窗口移动事件并更新控制台窗口位置
    threading.Thread(target=toolC.init_position, daemon=True).start()
    threading.Thread(target=toolC.run, daemon=True).start()

    # 启动主界面
    webview.start()

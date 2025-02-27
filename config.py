#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : config.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2025/2/27

import json
from pathlib import Path
from utils.rand import generate_random_uppercase


class Config:
    _game_title = f"元梦之星农场助手{' ' * 6}V1.8{' ' * 6}QQ交流群{' ' * 6}532285386"

    def __init__(self):
        self.access_code = self.init_access()
        self.game_title = self._game_title + f' 许可证:{self.access_code}'

    def get_game_title(self):
        return self.game_title + f' 授权码:{self.init_access()}'

    def init_access(self):
        store_path = Path('./game.json')
        try:
            # 先尝试读取现有文件
            with store_path.open('r', encoding='utf-8') as f:
                game_data = json.load(f)

            if access_code := game_data.get('access_code'):
                return access_code

            # 无有效访问码时生成并保存
            return self._update_access_code(store_path, game_data)

        except (FileNotFoundError, json.JSONDecodeError):
            # 文件不存在或内容无效时创建新文件
            return self._create_new_access_file(store_path)

        except Exception as e:
            print(f"Unexpected error: {e}")
            return self._create_new_access_file(store_path)

    def _create_new_access_file(self, path: Path) -> str:
        """创建包含新访问码的新文件"""
        access_code = generate_random_uppercase(8)
        self._save_access_code(path, {"access_code": access_code})
        return access_code

    def _update_access_code(self, path: Path, data: dict) -> str:
        """更新现有数据中的访问码"""
        access_code = generate_random_uppercase(8)
        data["access_code"] = access_code
        self._save_access_code(path, data)
        return access_code

    def _save_access_code(self, path: Path, data: dict):
        """通用保存方法"""
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : random.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2025/2/27

import random
import string


def generate_random_uppercase(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

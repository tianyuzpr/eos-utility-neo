#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EOS Utility Neo 配置文件"""


class Config:
    """应用配置类，所有配置项均为类变量（大写），供 Flask 的 from_object 加载。"""
    
    # Flask 基础配置
    DEBUG = False  # 生产环境默认关闭，后续通过 pywebview 启动时强制为 False
    SECRET_KEY = "your_secret_key"  # 生产环境请替换为随机字符串
    PRODUCTION = False
    PYWEBVIEW = False
    
    # 网络配置
    PORT = 23456
    HOST = "0.0.0.0"
    
    # 日志配置
    LOG_FILE = "logs/app.log"
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
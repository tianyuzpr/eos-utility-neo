#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EOS Utility Neo 主要 Flask 应用程序"""

# region Imports
import os
import logging

from flask import Flask, render_template, jsonify

import config

# endregion

# region Init

app = Flask(__name__)

# 加载配置
app.config.from_object(config.Config)

# 如果通过 pywebview 启动，强制关闭 debug 模式，避免热重载进程干扰
if app.config.get("PYWEBVIEW", False):
    app.config["DEBUG"] = False

# 日志配置
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename=app.config["LOG_FILE"],
    level=getattr(logging, app.config["LOG_LEVEL"]),
    format=app.config["LOG_FORMAT"]
)
logger = logging.getLogger(__name__)

logger.info("Flask app initialized with configuration: %s", app.config)

# endregion

# region Routes

@app.route("/")
def index():
    logger.info("Accessed index page")
    return render_template("index.html")

@app.route("/api/hello", methods=["GET"])
def hello():
    logger.info("Accessed hello endpoint")
    return jsonify({"message": "Hello, World!"})

# endregion

# region Main

if __name__ == "__main__":
    if app.config["PRODUCTION"]:
        print("Please use Gunicorn or other production server.")
    else:
        app.run(
            host=app.config["HOST"],
            port=app.config["PORT"],
            debug=app.config["DEBUG"]
        )
        logger.info(f"Flask app running on {app.config['HOST']}:{app.config['PORT']} with debug={app.config['DEBUG']}")

# endregion
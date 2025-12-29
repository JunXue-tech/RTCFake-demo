# 根目录的 conf.py - 仅用于 GitHub Actions
import os
import sys

# 将 source 目录添加到路径
sys.path.insert(0, os.path.abspath('.'))

# 导入真正的配置
from source.conf import *

# 调整 html_static_path
html_static_path = ['source/_static']
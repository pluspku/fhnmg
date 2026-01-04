#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fhnmg external package - 哨兵包，用于阻止从公共 PyPI 安装
此包在任何情况下都不应该被安装，会直接抛出错误
"""

from setuptools import setup
import os

# 直接抛出错误，不允许安装
raise RuntimeError(
    "\n" + "="*70 + "\n"
    "错误：您正在尝试从公共 PyPI 安装 fhnmg 包！\n"
    "="*70 + "\n"
    "fhnmg 是一个哨兵包，不应该从公共 PyPI 安装。\n"
    "请使用内部 PyPI index 安装。\n\n"
    "配置方法：\n"
    "1. 设置环境变量：\n"
    "   export PIP_INDEX_URL=https://pypi.fhnmg.cn/simple\n"
    "   export PIP_EXTRA_INDEX_URL=https://pypi.org/simple\n\n"
    "2. 或使用 pip config：\n"
    "   pip config set global.index-url https://pypi.fhnmg.cn/simple\n"
    "   pip config set global.extra-index-url https://pypi.org/simple\n\n"
    "3. 或在安装时指定：\n"
    "   pip install -i https://pypi.fhnmg.cn/simple fhnmg\n"
    "="*70 + "\n"
)

setup(
    name='fhnmg',
    version='1.0.0',
    description='哨兵包：检测是否使用了内部 PyPI index',
    long_description=open('README.md', encoding='utf-8').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    author='FH Team',
    author_email='',
    url='',
    packages=['fh'],
    namespace_packages=['fh'],
    python_requires='>=3.6',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)


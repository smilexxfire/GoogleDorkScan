from pathlib import Path

from config.log import logger
import platform
from distutils.version import LooseVersion
import re

def check_dep():
    logger.log('INFOR', 'Checking dependent environment')
    implementation = platform.python_implementation()
    version = platform.python_version()
    if implementation != 'CPython':
        logger.log('FATAL', f'GoogleDorkScan only passed the test under CPython')
        exit(1)
    if LooseVersion(version) < LooseVersion('3.6'):
        logger.log('FATAL', 'GoogleDorkScan requires Python 3.6 or higher')
        exit(1)

def save_to_file(filename):
    pass

def is_valid_url(url):
    # 匹配 URL 格式的正则表达式
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(url_pattern, url) is not None
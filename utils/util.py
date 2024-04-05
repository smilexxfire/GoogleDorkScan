from pathlib import Path

from config.log import logger
import platform
from distutils.version import LooseVersion

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
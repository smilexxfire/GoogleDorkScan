import time
from datetime import datetime

from googlesearch import search

from utils import util
from config.log import logger
from config.config import *
import fire

yellow = '\033[01;33m'
white = '\033[01;37m'
green = '\033[01;32m'
blue = '\033[01;34m'
red = '\033[1;31m'
end = '\033[0m'

version = 'v1.0.0'
message = white + '{' + red + version + ' #main' + white + '}'

googledarkscan_banner = f"""
GoogleDorkScan is a tool that assists in google dork{yellow}
  ____                   _      ____             _     ____   ____            
 / ___| ___   ___   __ _| | ___|  _ \  __ _ _ __| | __/ ___| / ___|__ _ _ __  {message}{green}
| |  _ / _ \ / _ \ / _` | |/ _ \ | | |/ _` | '__| |/ /\___ \| |   / _` | '_ \ {blue}
| |_| | (_) | (_) | (_| | |  __/ |_| | (_| | |  |   <  ___) | |__| (_| | | | |{white}
 \____|\___/ \___/ \__, |_|\___|____/ \__,_|_|  |_|\_\|____/ \____\__,_|_| |_|{yellow}
                   |___/                                                      
"""
class GoogleDorkScan(object):
    """
    GoogleDorkScan help summary page

    GoogleDorkScan is a tool that assists in google dork

    Example:
        python3 googledorkscan.py --target example.com run
    """
    def __init__(self, target=None, pagesize=5):
        self.target = target
        self.pagesize = pagesize
    def config_param(self):
        pass
    def check_param(self):
        """
        Check parameter
        """
        if self.target is None:
            logger.log('FATAL', 'You must provide either target or targets parameter')
            exit(1)

    def main(self):
        """main process

        :return:
        """
        logger.log('ALERT', "Checking Login Page")
        for login in login_pages.keys():
            query = f"site:{self.target} {login_pages[login]}"
            logger.log('ALERT', "Google query: " + query)
            url_list = list()
            for url in search(query, stop=self.pagesize):
                url_list.append(url)
            if len(url_list) == 0:
                logger.log('ALERT', "No results")
            else:
                for _ in url_list:
                    logger.log('INFOR', _)
            time.sleep(10)

        logger.log('ALERT', "Checking file leak")
        for file_key in file_types.keys():
            query = f"site:{self.target} {file_types[file_key]}"
            logger.log('INFOR', "Google query: " + query)
            url_list = list()
            for url in search(query, stop=self.pagesize):
                url_list.append(url)
            if len(url_list) == 0:
                logger.log('ALERT', "No results")
            else:
                for _ in url_list:
                    logger.log('INFOR', _)
            time.sleep(10)

        logger.log('ALERT', "Checking dir traversal")
        for dir_key in dir_traversal.keys():
            query = f"site:{self.target} {dir_traversal[dir_key]}"
            logger.log('INFOR', "Google query: " + query)
            url_list = list()
            for url in search(query, stop=self.pagesize):
                url_list.append(url)
            if len(url_list) == 0:
                logger.log('ALERT', "No results")
            else:
                for _ in url_list:
                    logger.log('INFOR', _)
            time.sleep(10)


    def run(self):
        """running entrance

        :return: None
        :return:
        """
        print(googledarkscan_banner)
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[*] Starting GoogleDorkScan @ {dt}\n')
        logger.log('DEBUG', 'GoogleDorkScan ' + version)
        util.check_dep()
        logger.log('INFOR', 'Start running GoogleDorkScan')
        self.config_param()
        self.check_param()

        self.main()

if __name__ == '__main__':
    fire.Fire(GoogleDorkScan)
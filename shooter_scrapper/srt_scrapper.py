# -*- coding:utf-8 -*-
import os
import sys
import logging
import random
import time
import settings
import requests
import scrapy

class SrtScrapper(object):
    """docstring for SrtScrapper"""
    def __init__(self):
        super(SrtScrapper, self).__init__()
        self.logger = logging.getLogger('srt_scrapper')

    def yield_address(self, page, item):
        base_url = 'http://assrt.net/xml/sub/{}/{}{}.xml'.format(page, page, item)
        print('scrapy crawl srt_spider -a urls=' + base_url)
        os.system('scrapy crawl srt_spider -a urls=' + base_url)
        

    def count_item(self):
        page_limit = 623
        item_limit = 886
        page = 1
        item = 250
        # round_span = random.randint(10, 30)
        while page < page_limit:
            # if count == round_span:
            #     s = requests.Session() 
            #     round_span = random.randint(10, 30)
            #     count = 0
            page_num = str(page).zfill(3)
            item_num = str(item).zfill(3)
            self.yield_address(page_num, item_num)
            page += 1
            item += 1
            if item == 1000:
                item = 1
            # t = random.randint(1, 3)
            # time.sleep(t)
        if page > page_limit:
            return
        while item < item_limit:
            # if count == round_span:
            #     s = requests.Session() 
            #     round_span = random.randint(10, 30)
            #     count = 0
            item_num = str(item).zfill(3)
            self.yield_address(str(page), item_num)
            item += 1
            t = random.randint(1, 3)
            time.sleep(t)


if __name__ == '__main__':
    srt_scrapper = SrtScrapper()
    srt_scrapper.count_item()
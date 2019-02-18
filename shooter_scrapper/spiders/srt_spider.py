# -*- coding:utf-8 -*-
import scrapy
import urllib.request

class SrtSpider(scrapy.Spider):
    """docstring for SrtSpider"""
    name = 'srt_spider'

    # def __init__(self, arg):
    #   super(SrtSpider, self).__init__()
    #   self.urls = arg
    #   self.dict = []

    def start_requests(self):
        urls = getattr(self, 'urls', None)
        # for url in urls:
        yield scrapy.Request(url = urls, callback = self.parse)

    def parse(self, response):
        dicts = []
        for link in response.xpath('//*[@id="btn_download"]/@href').extract():
            filename = response.xpath('//*[@id="movietitle1"]/text()').extract()[0]
            filename = filename.replace('/', '_')
            url = 'http://assrt.net' + link
            dicts.append(url)
            print(url)
            try:
                urllib.request.urlretrieve(url, filename = '/Users/fqdl123/Downloads/srt字幕/shooter/' + filename + '.rar')
            except Exception as e:
                print("Error occurred when downloading file, error message:")
                print(e)


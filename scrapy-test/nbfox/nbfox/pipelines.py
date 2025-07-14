# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface

import json
from itemadapter import ItemAdapter  # noqa
import pymongo
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import time


# 存储到mongodb的pipeline
class NbfoxDataToMongoDBPipeline:

    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
        mydb = myclient["db_nbfox"]
        self.mycollection = mydb["collection_nbfox"]

    def process_item(self, item, spider):
        data = dict(item)
        self.mycollection.insert_one(data)
        return item


# 存储图片到本地的pipeline
# https://shahzaibchadhar.medium.com/how-to-use-scrapy-for-image-download-using-pipelines-in-python-37be4cce6c18
class NbfoxDownloadImagesPipeline(ImagesPipeline):
    default_headers = {
        'accept':
        'image/webp,image/*,*/*;q=0.8',
        'accept-encoding':
        'gzip, deflate, sdch, br',
        'accept-language':
        'zh-CN,zh;q=0.8,en;q=0.6',
        'cookie':
        'bid=yQdC/AzTaCw',
        'referer':
        'https://www.douban.com/photos/photo/2370443040/',
        'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def get_media_requests(self, item, info):
        print("====get_media_requests===")
        for image_url in item['image_urls']:
            self.default_headers['referer'] = image_url  #反扒手段
            yield scrapy.Request(image_url, headers=self.default_headers)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]

        if not image_paths:
            raise DropItem("Item contains no images")

        item['image_paths'] = image_paths
        item['download_time'] = time.time()

        return item


# 存储到本地文件的pipeline
class NbfoxDataTOLocalFilePipeline():

    def __init__(self):
        print("====__file__===", os.path.dirname(__file__))

        self.file_name = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'nbfox_data.json')
        self.handler = open(self.file_name, 'w')

    def process_item(self, item, spider):
        print("====process_item===")
        self.handler.write(json.dumps(dict(item)) + '\n')
        return item

    def close_spider(self, spider):
        self.handler.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

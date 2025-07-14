# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# 如何自动下载图片，保存到本地
# https://blog.csdn.net/qq_39579087/article/details/106182459

import scrapy


class NbfoxItem(scrapy.Item):
    tax_href = scrapy.Field()
    tax_title = scrapy.Field()
    title = scrapy.Field()
    information = scrapy.Field()
    detail_href = scrapy.Field()
    tag_list = scrapy.Field()
    content = scrapy.Field()
    #  https://blog.csdn.net/qq_39579087/article/details/106182459
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
    download_time = scrapy.Field()

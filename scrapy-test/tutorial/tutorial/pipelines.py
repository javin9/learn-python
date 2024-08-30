# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter  # noqa


class TutorialPipeline:

    def process_item(self, item, spider):
        print("这是我们获取到的数据", item)
        return item

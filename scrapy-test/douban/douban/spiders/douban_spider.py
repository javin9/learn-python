import scrapy
from scrapy import Request


class DoubanSpiderSpider(scrapy.Spider):
    name = "douban_spider"
    default_headers = {
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cookie':
        'll="118282"; bid=UptK4kDEzj0; ue="cnhacker499@163.com"; gr_user_id=72bc77c5-d8e3-400e-abd3-5833aae9f885; ap=1; _vwo_uuid_v2=F7FF3E3B4FF64E68D5236A13BA96204A|4dfe5cca086f3d59f4b36a85ed3a90b7; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1488266010%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D_DuWJ5rsiaxCIdv1pj1hT7ytR63fdl15ChB0apCmpGvCevamdZ5Ws3V2tBVh_tiI%26wd%3D%26eqid%3Dd372c3980001d16800000006589b21d9%22%5D; _pk_id.100001.8cb4=e321643b0837abd0.1480306554.80.1488266010.1487570926.; _pk_ses.100001.8cb4=*',
        'Host':
        'book.douban.com',
        'Pragma':
        'no-cache',
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        "referer":
        "https://book.douban.com/subject/36754770/?icn=index-topchart-subject"
    }

    allowed_domains = ["douban.com"]
    start_urls = [
        "https://book.douban.com/subject/36754770/?icn=index-topchart-subject"
    ]

    def start_requests(self):
        print("====start_requests====")
        for url in self.start_urls:
            yield Request(url=url,
                          headers=self.default_headers,
                          callback=self.parse)

    def parse(self, response):
        title = response.xpath(
            "//h1/span[@property='v:itemreviewed']/text()").extract_first()

        print("====title====", title)
        book_content = response.xpath(
            "//div[@id='link-report']/.//div[@class='intro']/p/text()"
        ).extract()

        print("====book_content====", book_content)
        author_description = response.xpath(
            "//div[@class='indent'][3]").extract_first()
        print("====author_description====", title, book_content,
              author_description)

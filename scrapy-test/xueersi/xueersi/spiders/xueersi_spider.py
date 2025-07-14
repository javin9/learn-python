import scrapy


class XueersiSpiderSpider(scrapy.Spider):
    name = "xueersi_spider"
    allowed_domains = ["www.xueersi.com"]
    start_urls = ["https://www.xueersi.com"]

    def parse(self, response):
        menu_list = response.xpath(
            "//div[@class='nav-list-item']/div/text()").extract()
        print("================", menu_list)

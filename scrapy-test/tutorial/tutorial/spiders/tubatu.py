import scrapy

from tutorial.items import TutorialItem


class TubatuSpider(scrapy.Spider):
    name = "tubatu"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        item_list = response.xpath('//div[@class="quote"]')
        for item in item_list:
            # ./ means the current node , .// means the current node and all its descendants
            # extract_first() is used to extract the first element
            # extract() is used to extract all elements
            result = {}
            result["title"] = item.xpath(
                './/span[@class="text"]/text()').extract_first()

            result["author"] = item.xpath(
                './/span/small[@class="author"]/text()').extract_first()
            result["href"] = item.xpath(".//span/a/@href").extract_first()

            # print(result, response.urljoin(result["href"]))
            yield scrapy.Request(url=response.urljoin(result["href"]),
                                 callback=self.parse_author,
                                 meta=result)

    def parse_author(self, response):
        content = response.xpath(
            '//div[@class="author-description"]/text()').extract_first()
        data = TutorialItem()
        data = {**response.request.meta, **{"content": content}}

        # print("测试结果内容，测试结果内容，测试结果内容，测试结果内容", data)

        yield data  # pipeline will be called

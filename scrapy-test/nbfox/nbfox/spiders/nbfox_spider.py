import scrapy

from nbfox.items import NbfoxItem


class NbfoxSpiderSpider(scrapy.Spider):
    name = "nbfox_spider"
    allowed_domains = ["www.nbfox.com"]
    start_urls = ["https://www.nbfox.com/topics/landscape/"]

    def parse(self, response):
        item_list = response.xpath("//article[contains(@class,'grid-item')]")
        for div_list in item_list:
            item = NbfoxItem()
            tax_href = div_list.xpath(
                ".//div[contains(@class,'entry-header-inner')]/.//a[@class='tax__link']/@href"
            ).extract_first()
            tax_title = div_list.xpath(
                ".//div[contains(@class,'entry-header-inner')]/.//a[@class='tax__link']/span/text()"
            ).extract_first()
            title = div_list.xpath(".//h2/a/text()").extract_first()
            detail_href = div_list.xpath(".//h2/a/@href").extract_first()
            information = div_list.xpath(
                "//div[@class='czr-wp-the-content']/p/text()").extract_first()

            tag_list = div_list.xpath(
                ".//ul[@class='tags']/li/a/span/text()").extract()
            item["tax_href"] = tax_href
            item["tax_title"] = tax_title
            item["title"] = title
            item["information"] = information
            item["detail_href"] = detail_href
            item["tag_list"] = tag_list

            yield scrapy.Request(url=response.urljoin(detail_href),
                                 callback=self.parse_detail,
                                 meta=item)

        # meta-nav
        if (response.xpath('//span[contains("@class",nav-previous)]')):
            # 获取当前页码
            current_page = response.xpath(
                '//span[@class="page-numbers   current"]/text()'
            ).extract_first()
            next_page = int(current_page) + 1
            if next_page < 3:
                next_url = f'https://www.nbfox.com/topics/landscape/page/{next_page}/'
                yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        # print("====parse_detail====", response.request.meta)
        image_url = response.xpath(
            "//div[@class='czr-wp-the-content']/p[1]/a/@href").extract_first()
        content = response.xpath(
            "//div[@class='czr-wp-the-content']/p[2]/text()").extract_first()
        response.request.meta["image_urls"] = [image_url]
        response.request.meta["content"] = content

        yield response.request.meta

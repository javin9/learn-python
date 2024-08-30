from scrapy import cmdline

cmd_str = 'scrapy crawl nbfox_spider'
cmdline.execute(cmd_str.split(' '))

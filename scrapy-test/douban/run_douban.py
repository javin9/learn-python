from scrapy import cmdline

cmd_str = 'scrapy crawl douban_spider'
cmdline.execute(cmd_str.split(' '))

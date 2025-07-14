# from spider.spider import Spider

# 打断点，按F5，或者左侧的绿色三角形
# .*? 表示非贪婪匹配  ?关闭贪婪模式

from request_test.index import getIp, souhu, taoche, beautifulsoup4Test

if __name__ == '__main__':
    taoche()
    souhu()
    getIp()
    beautifulsoup4Test()
    # loadImage(
    #     "https://p6-passport.byteacctimg.com/img/user-avatar/47746f4cb87537c3b652b0e23582a8f4~80x80.awebp"
    # )
# spider = Spider('Spiderman')
# spider.crawl('https://top.baidu.com/board?tab=novel')

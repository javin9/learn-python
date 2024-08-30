from spider.playwright_test_demo import baidu_test
from playwright.sync_api import sync_playwright


def playwright_run():
    with sync_playwright() as playwright:
        baidu_test(playwright)

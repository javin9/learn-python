# import re
# from playwright.sync_api import Page

import time


def baidu_test(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com")
    page.wait_for_selector(".s_btn")
    page.fill("#kw", "playwright")
    page.click(".s_btn")
    time.sleep(10000)


# from playwright.sync_api import sync_playwright

# def run(playwright):
#     browser = playwright.chromium.launch(headless=True)  # 在此设置无头模式
#     context = browser.new_context()
#     # 执行操作...
#     page = context.new_page()
#     page.goto('http://example.com')
#     print(page.title())
#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)

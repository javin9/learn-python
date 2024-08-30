from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.get_by_role("link", name="登录").click()
    page.get_by_placeholder("手机号/用户名/邮箱").click()
    page.get_by_placeholder("手机号/用户名/邮箱").fill("416918024")
    page.get_by_placeholder("密码").click()
    page.get_by_placeholder("密码").fill("abc1213")
    page.get_by_role("checkbox", name="阅读并接受").check()
    page.get_by_role("button", name="登录").click()
    page.locator(".passMod_slide-btn").click()
    page.locator(".passMod_slide-btn").click()
    page.locator(".passMod_slide-btn").click()
    page.locator(".passMod_slide-btn").click()
    page.get_by_text("|刷新").click()
    page.locator(".passMod_slide-btn").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

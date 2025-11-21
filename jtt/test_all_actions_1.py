import re
from playwright.sync_api import Playwright, sync_playwright, expect, Page


def test_t(page: Page) -> None:

    page.goto("https://letcode.in/test")
    page.get_by_role("link", name="Edit").click()
    # page.get_by_role("textbox", name="Enter first & last name").click()
    page.get_by_role("textbox", name="Enter first & last name").fill("asd")
    page.goto("https://letcode.in/test")
    print("debug here")
    page.get_by_role("link", name="Click").click()
    page.get_by_role("button", name="Goto Home and come back here").click()
    page.goto("https://letcode.in/test")
    page.get_by_role("link", name="Drop-Down").click()
    page.locator("#fruits").select_option("1")
    page.goto("https://letcode.in/test")
    page.get_by_role("link", name="Toggle").click()
    page.locator("#yes").check()
    page.get_by_text("Foo").click()
    page.get_by_role("checkbox", name="Remember me").uncheck()
    page.get_by_role("checkbox", name="I agree to the FAKE terms and").check()
    page.goto("https://letcode.in/test")
    page.get_by_role("link", name="AUI - 5").click()
    page.locator("#generate").fill("35")
    page.get_by_role("button", name="Get Countries").click()




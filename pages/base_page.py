from playwright.sync_api import Page
from config.settings import BASE_URL

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = ""):
        url = f"{BASE_URL}/{path.lstrip('/')}"
        self.page.goto(url)

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def click(self, locator: str):
        self.page.locator(locator).click()

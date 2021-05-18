import asyncio
from features.Page.Base_page import Browser
from features.Page.elements_page.amazon_elements import Amazon_Locations
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GooglePage:
    def __init__(self, Page):
        self.Page = Page

    def go_to_page(self, url):
        self.Page.goto(url)

    def search_google(self, name):
        self.Page.fill('input[name="q"]', name)
        self.Page.press('input[name="q"]', "Enter")

    def Validate_search(self):
        answer = self.Page.wait_for_selector('text=Amazon.com.br - Tudo para você de A a Z', timeout=30000,
                                             state="visible")
        assert answer

    def screenshot(self, name):
        self.Page.screenshot(path=name, full_page=True)

    def close_brownser(self):
        self.Page.close()

import asyncio
from features.Page.Base_page import Browser
from features.Page.elements_page.google_elements import Google_Locations
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import *
from features.utils.utils import Utils

class GooglePage(Browser):

    def go_to_page(self,url):
        self.driver.get(url)

    def search_google(self, name):
        elemento = Utils(self.driver).wait_element((By.CSS_SELECTOR,Google_Locations().TEXTBOX_PESQUISAR_GOOGLE))
        # elemento = self.driver.find_element(By.CSS_SELECTOR,Google_Locations().TEXTBOX_PESQUISAR_GOOGLE)
        elemento.send_keys(name)
        elemento.send_keys(Keys.ENTER)

    def validate_search(self,text):
        elemento = Utils(self.driver).wait_element((By.XPATH,Google_Locations().ELEMENTO_BUSCA_GOOGLE))
        # elemento = self.driver.find_element(By.XPATH,Google_Locations().ELEMENTO_BUSCA_GOOGLE).text
        assert text.lower() in elemento.lower()

    def screenshot(self,name):
        self.driver.save_screenshot(name)
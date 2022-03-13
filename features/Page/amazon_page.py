import asyncio
from features.Page.Base_page import Browser
from features.Page.elements_page.amazon_elements import Amazon_Locations
from features.Page.elements_page.google_elements import Google_Locations
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.utils.utils import Utils


class AmazonPage(Browser):

    def go_to_page(self):
        elemento = self.driver.find_element(By.XPATH, Google_Locations().ELEMENTO_BUSCA_GOOGLE)
        elemento.click()

    def search_amazon(self, name):
        elemento = self.driver.find_element(By.ID, Amazon_Locations().CAIXA_PESQUISA)
        elemento.send_keys(name)
        elemento.send_keys(Keys.ENTER)

    def validate_search(self, texto):
        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, Amazon_Locations.PESQUISA_RESULTADO)))
        elemento = element.text
        assert texto.lower() in elemento.replace('"', '').lower()

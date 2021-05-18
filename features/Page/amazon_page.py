import asyncio
from features.Page.Base_page import Browser
from features.Page.elements_page.amazon_elements import Amazon_Locations
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AmazonPage(Browser):

    def go_to_page(self):
        elemento = self.driver.find_element(By.XPATH,Amazon_Locations.ELEMENTO_BUSCA_GOOGLE)
        elemento.click()

    def search_Amazon(self, name):
        elemento = self.driver.find_element(By.ID,Amazon_Locations.CAIXA_PESQUISA)
        elemento.send_keys(name)
        elemento.send_keys(Keys.ENTER)

    def Validate_search(self,text):
        elemento = self.driver.find_element(By.CSS_SELECTOR,Amazon_Locations.PESQUISA_RESULTADO)
        texto_elemento = elemento.text
        assert texto_elemento == f'"{text}"'

    def screenshot(self, name):
        self.driver.save_screenshot('Amazon.png')
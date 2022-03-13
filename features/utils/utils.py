from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Utils:
    def __init__(self, drive):
        self.driver = drive

    def search_element(self, search_method):
        return self.driver.find_element(search_method)

    def wait_element(self, search_method, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(search_method))
            return element
        except:
            return False

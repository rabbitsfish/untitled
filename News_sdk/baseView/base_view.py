from selenium.webdriver.support.ui import WebDriverWait
import logging
from selenium.common.exceptions import TimeoutException
class BaseView:
    def __init__(self, driver):
        self.driver = driver

    def find_element_news(self, loc):
        try:
            elem = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
            return elem
        except TimeoutException as e:
            logging.info(e.msg)
            return False

    def find_elements_news(self, loc):
        try:
            elems = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))
            return elems
        except TimeoutException as e:
            logging.info(e.msg)
            return False
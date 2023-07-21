from selenium import webdriver
from selenium.webdriver import Keys
from signin.locators import Locators
from selenium.webdriver.common.by import By
import logging

LOGGER = logging.getLogger(__name__)

class Element:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = self.driver.find_element(self.locator[0], self.locator[1])
        # shadow_div = driver.find_element(By.ID, "frontegg-login-box-container-default")
        # self.element = shadow_div.shadow_root.find_element(self.locator[0], self.locator[1])

    def click_element(self):
        self.element.click()

class InputElement(Element):
    def enter_text(self, text):
        LOGGER.debug(f"Получен и введен в поле текст: '{text}'")
        self.click_element()
        self.element.send_keys(text)

    def key_code(self):
        return self.element.send_keys(Keys.ENTER)

    def get_text(self):
        return self.element.get_attribute('value')
class ButtonElement(Element):
    def key_code(self):
        return self.element.send_keys(Keys.ENTER)
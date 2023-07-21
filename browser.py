from selenium import webdriver
import logging

LOGGER = logging.getLogger(__name__)

class Browser:
    def __init__(self, base_url='https://cloud.scylladb.com'):
        LOGGER.info("Браузер Chrome запущен")
        self.driver = webdriver.Chrome()
        self.base_url = base_url

    def go_to_site(self, path):
        signUp_url = self.base_url + path
        LOGGER.info(f"Переход по заданному URL: {signUp_url}")
        return self.driver.get(signUp_url)

    def go_to_url(self, url):
        return self.driver.get(url)

    def get_driver(self):
        return self.driver

    def close_browser(self):
        return self.driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from signin.element import Element, InputElement, ButtonElement
from signin.locators import Locators
import random
import string
import logging

LOGGER = logging.getLogger(__name__)

class User:
    def __init__(self, email):
        self.email = email

    @staticmethod
    def generate_password(count_special_chars, count_letters, count_numbers):
        special_chars = random.sample(string.punctuation, count_special_chars)
        letters = random.sample(string.ascii_letters, count_letters)
        numbers = random.sample(string.digits, count_numbers)
        password = special_chars + letters + numbers
        return password

    def password(self):
        self.password = self.generate_password(count_special_chars=1, count_letters=2, count_numbers=5)
        return self.password


class SignIn():
    path = '/account/login'

    def __init__(self, browser):
        self.email = InputElement(driver=browser.get_driver(), locator=Locators.email_locator)
        self.password = InputElement(driver=browser.get_driver(), locator=Locators.password_locator)
        self.signin_button = ButtonElement(driver=browser.get_driver(), locator=Locators.signin_button_locator)

    def signin(self, user: User):
        self.email.enter_text(user.email)
        self.password.enter_text(user.password)
        self.signin_button.key_code()
        LOGGER.info("Регистрация завершена")

from selenium import webdriver
from selenium.webdriver.common.by import By
from signUp.element import Element, InputElement, ButtonElement
from signUp.locators import Locators
import logging

LOGGER = logging.getLogger(__name__)

class User:
    def __init__(self, company_email, first_name, last_name, company):
        self.company_email = company_email
        self.first_name = first_name
        self.last_name = last_name
        self.company = company


class SignUp():
    path = '/account/sign-up'
    def __init__(self, browser):
        self.company_email = InputElement(driver=browser.get_driver(), locator=Locators.company_email_locator)
        self.first_name = InputElement(driver=browser.get_driver(), locator=Locators.first_name_locator)
        self.last_name = InputElement(driver=browser.get_driver(), locator=Locators.last_name_locator)
        self.company = InputElement(driver=browser.get_driver(), locator=Locators.company_locator)
        self.signup_button = ButtonElement(driver=browser.get_driver(), locator=Locators.signup_button_locator)

    def signup(self, user: User):
        LOGGER.info("Начинаем регистрацию")
        self.company_email.enter_text(user.company_email)
        self.first_name.enter_text(user.first_name)
        self.last_name.enter_text(user.last_name)
        self.company.enter_text(user.company)
        self.signup_button.key_code()
        LOGGER.info("Регистрация завершена")
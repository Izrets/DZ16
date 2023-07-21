from selenium.webdriver.common.by import By


class Locators:
    company_email_locator = (By.NAME, 'email')
    first_name_locator = (By.NAME, 'firstName')
    last_name_locator = (By.NAME, 'lastName')
    company_locator = (By.NAME, 'companyName')
    signup_button_locator = (By.CLASS_NAME, 'MuiLoadingButton-root')

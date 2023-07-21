from selenium.webdriver.common.by import By

class Locators:
    # email_locator = (By.NAME, 'email')
    # password_locator = (By.NAME, 'password')
    # signin_button_locator = (By.CLASS_NAME, 'MuiLoadingButton-root')

    email_locator = (By.XPATH, '//*[@id="frontegg-login-box-container-default"]/div[3]/input')
    password_locator = (By.XPATH, '//*[@id="frontegg-login-box-container-default"]/div[4]/input')
    signin_button_locator = (By.XPATH, '//*[@id="frontegg-login-box-default"]/div[2]/div[1]/div/div/div/div/div/div[4]/div/div/form/button')

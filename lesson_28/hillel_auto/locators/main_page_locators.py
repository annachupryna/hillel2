from selenium.webdriver.common.by import By


class MainPageLocators:

    sign_up_button = (By.XPATH, '//button[@class="hero-descriptor_btn btn btn-primary"]')
    name_field = (By.XPATH, '//input[@id="signupName"]')
    last_name_field = (By.XPATH, '//input[@id="signupLastName"]')
    email_field = (By.XPATH, '//input[@id="signupEmail"]')
    password_field = (By.XPATH, '//input[@id="signupPassword"]')
    repeat_password_field = (By.XPATH, '//input[@id="signupRepeatPassword"]')
    register_button = (By.XPATH, '//button[@class="btn btn-primary"]')

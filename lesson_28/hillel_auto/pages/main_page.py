from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.hillel_auto.locators.main_page_locators import MainPageLocators
from lesson_28.hillel_auto.pages.account_page import AccountPage
from lesson_28.hillel_auto.pages.base_page import BasePage
from faker import Faker


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url='https://guest:welcome2qauto@qauto2.forstudy.space')

    def sign_up_button(self):
        return WebDriverWait(self.driver, timeout=2).until \
            (EC.presence_of_element_located(MainPageLocators.sign_up_button))

    def name_input(self):
        return WebDriverWait(self.driver, timeout=2).until \
            (EC.presence_of_element_located(MainPageLocators.name_field))

    def last_name_input(self):
        return WebDriverWait(self.driver, timeout=2).until \
            (EC.presence_of_element_located(MainPageLocators.last_name_field))

    def email_input(self):
        return WebDriverWait(self.driver, timeout=2).until \
            (EC.presence_of_element_located(MainPageLocators.email_field))

    def password_input(self):
        return WebDriverWait(self.driver, timeout=2).until \
            (EC.presence_of_element_located(MainPageLocators.password_field))

    def repeat_password_input(self):
        return WebDriverWait(self.driver, timeout=2).until \
            (EC.presence_of_element_located(MainPageLocators.repeat_password_field))

    def register_button(self):
        return WebDriverWait(self.driver, timeout=2).until \
            (EC.presence_of_element_located(MainPageLocators.register_button))

    def set_name(self, name):
        return self.name_input().send_keys(name)

    def set_last_name(self, last_name):
        return self.last_name_input().send_keys(last_name)

    def set_email(self, email):
        return self.email_input().send_keys(email)

    def set_password(self, password):
        return self.password_input().send_keys(password)

    def set_repeat_password(self, password):
        return self.repeat_password_input().send_keys(password)

    def click_sign_up_button(self):
        return self.sign_up_button().click()

    def click_register_button(self):
        return self.register_button().click()

    def register(self) -> AccountPage:
        fake = Faker()
        password = fake.password(length=10)
        self.click_sign_up_button()
        self.set_name(fake.first_name())
        self.set_last_name(fake.last_name())
        self.set_email(fake.email())
        self.set_password(password)
        self.set_repeat_password(password)
        self.click_register_button()
        return AccountPage(self.driver)

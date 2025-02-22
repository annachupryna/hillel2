from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.hillel_auto.locators.account_page_locators import AccountPageLocators
from lesson_28.hillel_auto.pages.base_page import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url='https://guest:welcome2qauto@qauto2.forstudy.space')

    def account_dropdown_present(self):
        return WebDriverWait(self.driver, timeout=2).until \
            (EC.presence_of_element_located(AccountPageLocators.account_dropdown_locator))

from lesson_27.nova_post import locators
from lesson_27.nova_post.locators import parcel_tracking_page_locators
from lesson_27.nova_post.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_27.nova_post.locators.parcel_tracking_page_locators import ParcelTrackingPageLocators


class ParcelTrackingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url='https://tracking.novaposhta.ua/#/uk')

    def input_tracking_field(self):
        return WebDriverWait(self.driver, timeout=2).until \
            (EC.presence_of_element_located(ParcelTrackingPageLocators.tracking_number_input_locator))

    def input_tracking_button(self):
        return WebDriverWait(self.driver, timeout=5).until \
            (EC.presence_of_element_located(ParcelTrackingPageLocators.search_button_locator))

    def set_tracking_number(self, tracking_number):
        return self.input_tracking_field().send_keys(tracking_number)

    def click_tracking_button(self):
        return self.input_tracking_button().click()

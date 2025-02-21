import pytest
import selenium
from lesson_27.nova_post.pages import parcel_tracking_page
from lesson_27.nova_post.pages.parcel_tracking_page import ParcelTrackingPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_27.nova_post.locators.parcel_tracking_page_locators import ParcelTrackingPageLocators


def test_input_tracking_number(driver):

    tracking_page = ParcelTrackingPage(driver)
    tracking_page.open_page()
    tracking_page.set_tracking_number('222222222222222')
    tracking_page.click_tracking_button()

    WebDriverWait(driver, timeout=4).until\
        (EC.text_to_be_present_in_element
         (ParcelTrackingPageLocators.parcel_not_fount_locator, 'Щось пішло не так'))









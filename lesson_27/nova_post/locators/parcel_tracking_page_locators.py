from selenium.webdriver.common.by import By


class ParcelTrackingPageLocators:

    tracking_number_input_locator = (By.XPATH, '//input[@class="track__form-group-input"]')
    search_button_locator = (By.XPATH, '//input[@class="track__form-group-btn green-active"]')
    parcel_not_fount_locator = (By.XPATH, '//div[@class="error-block__title"]')

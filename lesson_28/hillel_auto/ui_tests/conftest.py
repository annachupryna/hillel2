import pytest
from selenium.webdriver import Chrome
from lesson_28.hillel_auto.pages.main_page import MainPage


@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()


@pytest.fixture()
def main_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    return main_page

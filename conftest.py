import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    page = MainPage(driver)
    return page

@pytest.fixture(scope='function')
def order_page(driver):
    page = OrderPage(driver)
    return page
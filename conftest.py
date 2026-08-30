import pytest
from selenium import webdriver
from locators import TestDescriptionOfElements as element
from urls import Urls as urls

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver_register(driver):
    driver.get(urls.url_register)
    yield driver

@pytest.fixture(scope="function")
def driver_main_page(driver):
    driver.get(urls.url_main)
    yield driver

@pytest.fixture(scope="function")
def driver_password_recovery_form(driver):
    driver.get(urls.url_password_recovery)
    yield driver

@pytest.fixture(scope="function")
def driver_login_page(driver):
    driver.get(urls.url_login)
    yield driver

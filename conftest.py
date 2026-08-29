import pytest
from selenium import webdriver
import random as r

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture(scope="function")
def driver_register(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    return driver

@pytest.fixture(scope="function")
def driver_main_page(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    return driver

@pytest.fixture(scope="function")
def driver_password_recovery_form(driver):
    driver.get("https://stellarburgers.education-services.ru/forgot-password")
    return driver

@pytest.fixture(scope="function")
def driver_login_page(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    return driver

@pytest.fixture(scope="function")
def name_login_password_random():
    name = "Ваня" + str(r.randint(100, 9999))
    login = str(r.randint(100, 9999)) + "@ya.ru"
    password = "123asd"
    name_login_password_random = {
        "name": name,
        "login": login,
        "password": password
    }
    return name_login_password_random

@pytest.fixture(scope="function")
def login_password():
    login_password = {
        "login": "124567@ya.ru",
        "password": "123asd"
    }
    return login_password

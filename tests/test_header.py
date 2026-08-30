from selenium.webdriver.common.by import By

from locators import TestDescriptionOfElements as element
from urls import Urls as urls

class TestGoToHeader():
    # переход по клику на «Личный кабинет»
    def test_to_profile_from_main(self, driver_main_page):
        driver_main_page.find_element(By.CSS_SELECTOR, element.button_header_profile_selector).click()
        assert driver_main_page.current_url == urls.url_login

    # переход по клику на «Конструктор»
    def test_transition_by_constructor_from_profile(self, driver_login_page):
        driver_login_page.find_element(By.CSS_SELECTOR, element.button_header_constructor_selector).click()
        assert driver_login_page.current_url == urls.url_main

    # переход по клику на логотип Stellar Burgers
    def test_transition_by_logo_from_profile(self, driver_login_page):
        driver_login_page.find_element(By.CSS_SELECTOR, element.button_header_logo_selector).click()
        assert driver_login_page.current_url == urls.url_main

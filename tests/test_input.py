from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestDescriptionOfElements as element
from urls import Urls as urls
from user_data import UserData as data

class TestGoToInputPage():
    # вход по кнопке на главной
    def test_login_from_main_page(self, driver_main_page):   
        driver_main_page.find_element(By.CSS_SELECTOR, element.button_input_main_page_selector).click()   
        self.data_entry(driver_main_page)

    # вход через личный кабинет
    def test_login_from_profile(self, driver_main_page):            
        driver_main_page.find_element(By.CSS_SELECTOR, element.button_header_profile_selector).click()
        self.data_entry(driver_main_page)

    # вход через форму регистрации
    def test_login_from_registration_form(self, driver_register):         
        driver_register.find_element(By.CSS_SELECTOR, element.button_input_from_registration_selector).click()   
        self.data_entry(driver_register)

    # вход через форму восстановления
    def test_login_from_password_recovery_form(self, driver_password_recovery_form):    
        driver_password_recovery_form.find_element(By.CSS_SELECTOR, element.button_input_password_recovery_form_selector).click()   
        self.data_entry(driver_password_recovery_form)

    def data_entry(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.button_input_page_input_path)))
        driver.find_element(By.NAME, element.login_for_input_page_input_name).send_keys(data.login_password()["login"])
        driver.find_element(By.NAME, element.password_for_input_page_input_name).send_keys(data.login_password()["password"])
        driver.find_element(By.XPATH, element.button_input_page_input_path).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.button_buns_main_page_path)))
        assert driver.current_url == urls.url_main
    
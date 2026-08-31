import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestDescriptionOfElements as element
from urls import Urls as urls
from user_data import UserData as data

class TestGoToInputPage():
    text = 'Оформить заказ'

    # Вход с главной страницы
    @pytest.mark.parametrize('button_on_main_page', 
                            [ element.button_input_main_page_selector, #по кнопке Войти
                              element.button_header_profile_selector   #по кнопке Личный кабинет
                            ])
    def test_login_from_main_page(self, driver_main_page, button_on_main_page):   
        driver_main_page.find_element(By.CSS_SELECTOR, button_on_main_page).click()   
        WebDriverWait(driver_main_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.button_input_page_input_path)))
        driver_main_page.find_element(By.NAME, element.login_for_input_page_input_name).send_keys(data.login_password()["login"])
        driver_main_page.find_element(By.NAME, element.password_for_input_page_input_name).send_keys(data.login_password()["password"])
        driver_main_page.find_element(By.XPATH, element.button_input_page_input_path).click()
        WebDriverWait(driver_main_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.button_order_path)))
        assert driver_main_page.find_element(By.XPATH, element.button_order_path).text == self.text

    # вход через форму регистрации
    def test_login_from_registration_form(self, driver_register):         
        driver_register.find_element(By.CSS_SELECTOR, element.button_input_from_registration_selector).click()   
        WebDriverWait(driver_register, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.button_input_page_input_path)))
        driver_register.find_element(By.NAME, element.login_for_input_page_input_name).send_keys(data.login_password()["login"])
        driver_register.find_element(By.NAME, element.password_for_input_page_input_name).send_keys(data.login_password()["password"])
        driver_register.find_element(By.XPATH, element.button_input_page_input_path).click()
        WebDriverWait(driver_register, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.button_order_path)))
        assert driver_register.find_element(By.XPATH, element.button_order_path).text == self.text

    # вход через форму восстановления
    def test_login_from_password_recovery_form(self, driver_password_recovery_form):    
        driver_password_recovery_form.find_element(By.CSS_SELECTOR, element.button_input_password_recovery_form_selector).click()   
        WebDriverWait(driver_password_recovery_form, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.button_input_page_input_path)))
        driver_password_recovery_form.find_element(By.NAME, element.login_for_input_page_input_name).send_keys(data.login_password()["login"])
        driver_password_recovery_form.find_element(By.NAME, element.password_for_input_page_input_name).send_keys(data.login_password()["password"])
        driver_password_recovery_form.find_element(By.XPATH, element.button_input_page_input_path).click()
        WebDriverWait(driver_password_recovery_form, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.button_order_path)))
        assert driver_password_recovery_form.find_element(By.XPATH, element.button_order_path).text == self.text

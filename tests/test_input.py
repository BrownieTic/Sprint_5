from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from description_of_elements import TestDescriptionOfElements as element

class TestGoToInputPage():
    # вход по кнопке на главной
    def test_login_from_main_page(self, driver_main_page, login_password):   
        driver_main_page.find_element(By.CSS_SELECTOR, element.button_input_main_page_selector).click()   
        self.data_entry(driver_main_page, login_password)

    # вход через личный кабинет
    def test_login_from_profile(self, driver_main_page, login_password):            
        driver_main_page.find_element(By.CSS_SELECTOR, element.button_header_profile_selector).click()
        self.data_entry(driver_main_page, login_password)

    # вход через форму регистрации
    def test_login_from_registration_form(self, driver_register, login_password):         
        driver_register.find_element(By.CSS_SELECTOR, element.button_input_from_registration_selector).click()   
        self.data_entry(driver_register, login_password)

    # вход через форму восстановления
    def test_login_from_password_recovery_form(self, driver_password_recovery_form, login_password):    
        driver_password_recovery_form.find_element(By.CSS_SELECTOR, element.button_input_password_recovery_form_selector).click()   
        self.data_entry(driver_password_recovery_form, login_password)

    def data_entry(self, driver_main_page, login_password):
        WebDriverWait(driver_main_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.button_input_page_input_path)))
        driver_main_page.find_element(By.NAME, element.login_for_input_page_input_name).send_keys(login_password["login"])
        driver_main_page.find_element(By.NAME, element.password_for_input_page_input_name).send_keys(login_password["password"])
        driver_main_page.find_element(By.XPATH, element.button_input_page_input_path).click()
        driver_main_page.quit()
    
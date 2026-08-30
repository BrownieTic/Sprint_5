from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from description_of_elements import TestDescriptionOfElements as element

class TestLogout:
    def test_logout_from_profile(self, driver_login_page, login_password):
        driver_login_page.find_element(By.NAME, element.login_for_input_page_input_name).send_keys(login_password["login"])
        driver_login_page.find_element(By.NAME, element.password_for_input_page_input_name).send_keys(login_password["password"])
        driver_login_page.find_element(By.XPATH, element.button_input_page_input_path).click()
        WebDriverWait(driver_login_page, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, element.button_header_profile_selector)))
        driver_login_page.find_element(By.CSS_SELECTOR, element.button_header_profile_selector).click()
        WebDriverWait(driver_login_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.button_out_profile_page_path)))
        driver_login_page.find_element(By.XPATH, element.button_out_profile_page_path).click()
        driver_login_page.quit()

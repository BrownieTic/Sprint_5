from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from description_of_elements import TestDescriptionOfElements as element

#успешная регистрация
def test_valid_registration(driver_register, name_login_password_random): 
    driver_register.find_element(By.XPATH, element.name_for_registration_path).send_keys(name_login_password_random["name"])
    driver_register.find_element(By.XPATH, element.login_for_registration_path).send_keys(name_login_password_random["login"])
    driver_register.find_element(By.XPATH, element.password_for_registration_path).send_keys(name_login_password_random["password"])
    driver_register.find_element(By.XPATH, element.button_register_path).click()
    WebDriverWait(driver_register, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.button_input_page_input_path)))
    assert driver_register.current_url == element.url_login
    driver_register.quit()

#ошибка регистрации с недопустимым коротким паролем
def test_invalid_password_registration(driver_register, name_login_password_random): 
    driver_register.find_element(By.XPATH, element.name_for_registration_path).send_keys(name_login_password_random["name"])
    driver_register.find_element(By.XPATH, element.login_for_registration_path).send_keys(name_login_password_random["login"])
    driver_register.find_element(By.XPATH, element.password_for_registration_path).send_keys("123")
    driver_register.find_element(By.XPATH, element.button_register_path).click()
    WebDriverWait(driver_register, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, element.password_erroror_registration_selector)))
    error_element = driver_register.find_element(By.CSS_SELECTOR, element.password_erroror_registration_selector).text
    error_text = 'Некорректный пароль'
    assert error_text in error_element
    driver_register.quit()

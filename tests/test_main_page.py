from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from description_of_elements import TestDescriptionOfElements as element

class TestMainPageSection:
    def test_to_sauces_sauces(self, driver_main_page):
        driver_main_page.find_element(By.XPATH, element.button_sauces_main_page_path).click()
        WebDriverWait(driver_main_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.section_sauces_main_page_path)))
        assert driver_main_page.find_element(By.XPATH, element.section_sauces_main_page_path).is_displayed()
        driver_main_page.quit()

    def test_to_section_fillings(self, driver_main_page):
        driver_main_page.find_element(By.XPATH, element.button_fillings_main_page_path).click()
        WebDriverWait(driver_main_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.section_fillings_main_page_path)))
        assert driver_main_page.find_element(By.XPATH, element.section_fillings_main_page_path).is_displayed()
        driver_main_page.quit()

    def test_to_section_buns(self, driver_main_page):
        driver_main_page.find_element(By.XPATH, element.button_fillings_main_page_path).click()
        driver_main_page.find_element(By.XPATH, element.button_buns_main_page_path).click()
        WebDriverWait(driver_main_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, element.section_buns_main_page_path)))
        assert driver_main_page.find_element(By.XPATH, element.section_buns_main_page_path).is_displayed()
        driver_main_page.quit()

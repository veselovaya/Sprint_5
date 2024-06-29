from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestConstructor:
    def test_click_on_sauces_in_constructor(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAKE_BURGER_TITLE))
        active_button = driver.find_element(*Locators.SAUCES_BUTTON)
        active_button.click()
        assert 'current' in active_button.get_attribute('class')


    def test_click_on_buns_in_constructor(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAKE_BURGER_TITLE))
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        active_button = driver.find_element(*Locators.BUNS_BUTTON)
        active_button.click()
        assert 'current' in active_button.get_attribute('class')


    def test_click_on_topping_in_constructor(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAKE_BURGER_TITLE))
        active_button = driver.find_element(*Locators.TOPPING_BUTTON)
        active_button.click()
        assert 'current' in active_button.get_attribute('class')
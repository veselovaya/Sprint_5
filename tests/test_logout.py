from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestLogout:
    def test_logout_with_button_exit(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_HEADER))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert driver.find_element(*Locators.LOGIN_BUTTON).text == 'Войти'
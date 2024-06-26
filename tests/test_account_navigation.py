from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestAccountNavigation:
    def test_transfer_to_personal_acc(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_HEADER)).text == 'Профиль'


    def test_from_account_to_constructor(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON_IN_HEADER).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAKE_BURGER_TITLE)).text == 'Соберите бургер'


    def test_from_account_to_main_label(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        driver.find_element(*Locators.STELLAR_BURGERS_LOGO).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MAKE_BURGER_TITLE)).text == 'Соберите бургер'



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestAuthorization:

    def test_authorize_enter_account_button_on_main(self, driver):
        email = 'nastya_veselova_10133@ya.ru'
        password = '123456'

        driver.find_element(*Locators.LOGIN_ON_MAIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.LOGIN_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_HEADER)).text == 'Профиль'


    def test_authorize_personal_account_button(self, driver):
        email = 'nastya_veselova_10133@ya.ru'
        password = '123456'

        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.LOGIN_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_HEADER)).text == 'Профиль'


    def test_authorize_login_button_in_registration_page(self, driver):
        email = 'nastya_veselova_10133@ya.ru'
        password = '123456'

        driver.find_element(*Locators.LOGIN_ON_MAIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.REGISTER_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_TITLE))
        driver.find_element(*Locators.LOGIN_BUTTON_ON_REGISTR_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.LOGIN_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_HEADER)).text == 'Профиль'


    def test_authorize_with_restore_password_button(self, driver):
        email = 'nastya_veselova_10133@ya.ru'
        password = '123456'
        driver.find_element(*Locators.LOGIN_ON_MAIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.RESTORE_PASSWRD_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_ON_REGISTR_FORM)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.LOGIN_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_HEADER)).text == 'Профиль'




from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from faker import Faker

faker = Faker()

class TestRegistration:

    def test_registration_true(self, driver):
        email = faker.email()
        password = '1234567'
        name = 'Настя'
        print(email)

        driver.find_element(*Locators.LOGIN_ON_MAIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.REGISTER_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_TITLE))

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTER_NAME))
        driver.find_element(*Locators.REGISTER_NAME).send_keys(name)
        driver.find_element(*Locators.REGISTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.LOGIN_INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.LOGIN_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE_HEADER))
        assert driver.find_element(*Locators.PROFILE_HEADER).text == 'Профиль'

    def test_registration_invalid_password(self, driver):
        email = faker.email()
        name = 'Настя'
        print(email)
        inv_password = '123'
        driver.find_element(*Locators.LOGIN_ON_MAIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.REGISTER_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_TITLE))
        driver.find_element(*Locators.REGISTER_NAME).send_keys(name)
        driver.find_element(*Locators.REGISTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(inv_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INVALID_PSW_MISTAKE)).text == 'Некорректный пароль'


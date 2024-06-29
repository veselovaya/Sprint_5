import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser

    browser.quit()


@pytest.fixture()
def login(driver):
    driver.find_element(*Locators.LOGIN_ON_MAIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
    driver.find_element(*Locators.LOGIN_INPUT_EMAIL).send_keys('nastya_veselova_10133@ya.ru')
    driver.find_element(*Locators.LOGIN_INPUT_PASSWORD).send_keys('123456')
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver



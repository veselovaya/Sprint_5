from selenium.webdriver.common.by import By

class Locators:
    LOGIN_ON_MAIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') #кнопка "Войти в аккаунт" на главной
    REGISTRATION_TITLE =(By.XPATH, '//h2[text()="Регистрация"]') #надпись "Регистрация"
    REGISTER_LINK =(By.XPATH, '//a[text()="Зарегистрироваться"]') #гиперссылка "Зарегистрироваться"
    REGISTER_NAME = (By.XPATH, '//label[text()="Имя"]/following-sibling::input') #инпут  ввода имени при регистрации
    REGISTER_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input') #инпут ввода email при регистрации
    PASSWORD = (By.NAME, 'Пароль') #инпут ввода пароля при регистрации
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]') #кнопка "Зарегистрироваться"
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]') #кнопка "Войти" на отдельной странице
    PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]') #кнопка "Личный Кабинет" в хэдере
    PROFILE_HEADER = (By.XPATH, '//a[text()="Профиль"]') #заголовок "Профиль" на странице личного кабинета
    LOGIN_INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input') # инпут ввода емейла для логина
    LOGIN_INPUT_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input') # инпут ввода пароля для логина
    INVALID_PSW_MISTAKE = (By.XPATH, '//p[text() = "Некорректный пароль"]') # текст ошибки
    LOGIN_BUTTON_ON_REGISTR_FORM = (By.XPATH, '//a[@href = "/login"]') #гиперссылка "Войти" на форме регистрации
    RESTORE_PASSWRD_BUTTON = (By.XPATH, '//a[@href = "/forgot-password"]') #гиперссылка "Восстановить пароль"
    CONSTRUCTOR_BUTTON_IN_HEADER = (By.XPATH, '//p[text()="Конструктор"]') #кнопка "Конструктор" в хэдере
    MAKE_BURGER_TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]') # заголовок "Соберите бургер" на главной
    STELLAR_BURGERS_LOGO = (By.XPATH, '//div[contains(@class, "logo")]/a[@href="/"]') # кнопка-лого сайта в хэдере
    EXIT_BUTTON = (By.XPATH, '//button[text() = "Выход"]') # кнопка "Выход" в профиле
    SAUCES_BUTTON = (By.XPATH, '//span[text()="Соусы"]/parent::div') # вкладка "Соусы"
    TOPPING_BUTTON = (By.XPATH, '//span[text()="Начинки"]/parent::div') # вкладка "Начинки"
    BUNS_BUTTON = (By.XPATH, '//span[text()="Булки"]/parent::div') # вкладка "Булки"












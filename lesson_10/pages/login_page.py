from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Page Object для страницы авторизации SauceDemo."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self) -> None:
        """
        Открывает страницу авторизации.

        """
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему.

        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Page Object для страницы медленного калькулятора."""

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> "CalculatorPage":
        """
        Открывает страницу калькулятора.

        """
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """
        Устанавливает задержку вычисления в секундах.

        """
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, label: str) -> "CalculatorPage":
        """
        Нажимает кнопку калькулятора по её тексту.

        """
        locator = (By.XPATH, f"//span[text()='{label}']")
        self.driver.find_element(*locator).click()
        return self

    def wait_for_result(self, expected: str) -> "CalculatorPage":
        """
        Ожидает появления ожидаемого результата на экране.

        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )
        return self

    def get_result(self) -> str:
        """
        Возвращает текущий текст результата с экрана.

        """
        return self.driver.find_element(*self.SCREEN).text
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для страницы медленного калькулятора."""

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds: int):
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, label: str):
        locator = (By.XPATH, f"//span[text()='{label}']")
        self.driver.find_element(*locator).click()
        return self

    def wait_for_result(self, expected: str):
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )
        return self

    def get_result(self) -> str:
        return self.driver.find_element(*self.SCREEN).text
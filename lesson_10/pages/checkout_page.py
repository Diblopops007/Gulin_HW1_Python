from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name: str, last_name: str,
                  postal_code: str) -> None:
        """
        Заполняет форму данными покупателя.

        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def click_continue(self) -> None:
        """
        Нажимает кнопку Continue.

        """
        self.driver.find_element(*self.continue_button).click()

    def get_total(self) -> str:
        """
        Возвращает текст итоговой суммы заказа.

        """
        total_element = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(self.total_label)
        )
        return total_element.text
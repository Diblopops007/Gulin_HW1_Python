from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Page Object для страницы корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def click_checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа.

        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    def get_cart_items_count(self) -> int:
        """
        Возвращает количество товаров в корзине.

        """
        return len(self.driver.find_elements(*self.cart_items))
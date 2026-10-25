from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_buttons = {
            "backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "bolt_t_shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
        }
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_key: str):
        self.driver.find_element(*self.add_to_cart_buttons[product_key]).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
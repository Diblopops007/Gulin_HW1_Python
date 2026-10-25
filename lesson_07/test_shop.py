from selenium import webdriver
from lesson_07.pages.login_page import LoginPage
from lesson_07.pages.inventory_page import InventoryPage
from lesson_07.pages.cart_page import CartPage
from lesson_07.pages.checkout_page import CheckoutPage


def test_session_storage_auth():
    driver = webdriver.Firefox()

    try:
    
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart("backpack")
        inventory_page.add_product_to_cart("bolt_t_shirt")
        inventory_page.add_product_to_cart("onesie")
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Сергей", "Гулин", "300010")
        checkout_page.click_continue()

        total_text = checkout_page.get_total()

        assert total_text == "Total: $58.29"

    finally:
        driver.quit()
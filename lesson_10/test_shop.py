import allure
from selenium import webdriver
from lesson_10.pages.login_page import LoginPage
from lesson_10.pages.inventory_page import InventoryPage
from lesson_10.pages.cart_page import CartPage
from lesson_10.pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.title("Проверка оформления заказа с авторизацией")
@allure.description(
    "Тест проверяет полный сценарий покупки: авторизация, "
    "добавление трёх товаров в корзину, оформление заказа "
    "и проверка итоговой суммы $58.29."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_session_storage_auth():
    driver = webdriver.Firefox()

    try:
        with allure.step("Открыть страницу авторизации"):
            login_page = LoginPage(driver)
            login_page.open()

        with allure.step("Авторизоваться под standard_user"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить три товара в корзину"):
            inventory_page = InventoryPage(driver)
            inventory_page.add_product_to_cart("backpack")
            inventory_page.add_product_to_cart("bolt_t_shirt")
            inventory_page.add_product_to_cart("onesie")
            inventory_page.go_to_cart()

        with allure.step("Перейти к оформлению заказа"):
            cart_page = CartPage(driver)
            cart_page.click_checkout()

        with allure.step("Заполнить форму покупателя"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_form("Сергей", "Гулин", "300010")
            checkout_page.click_continue()

        with allure.step("Проверить итоговую сумму заказа"):
            total_text = checkout_page.get_total()
            assert total_text == "Total: $58.29"
    finally:
        driver.quit()
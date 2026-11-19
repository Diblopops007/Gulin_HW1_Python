import allure
from selenium import webdriver
from lesson_10.pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.title("Проверка работы медленного калькулятора")
@allure.description(
    "Тест проверяет, что калькулятор корректно выполняет сложение "
    "7 + 8 = 15 с установленной задержкой 45 секунд."
)
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator():
    driver = webdriver.Chrome()

    try:
        with allure.step("Открыть страницу калькулятора"):
            page = CalculatorPage(driver)
            page.open()

        with allure.step("Установить задержку 45 секунд"):
            page.set_delay(45)

        with allure.step("Выполнить сложение 7 + 8"):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        with allure.step("Дождаться результата '15'"):
            page.wait_for_result("15")

        with allure.step("Проверить, что результат равен '15'"):
            assert page.get_result() == "15"
    finally:
        driver.quit()
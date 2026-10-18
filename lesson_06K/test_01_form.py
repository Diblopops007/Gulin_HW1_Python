import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        first_name = wait.until(EC.visibility_of_element_located((By.NAME, "first-name")))
        first_name.send_keys("Иван")

        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()


        zip_code_field = wait.until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )

        assert "alert-danger" in zip_code_field.get_attribute("class"), \
            f"Поле Zip code не подсвечено красным, класс: {zip_code_field.get_attribute('class')}"

        valid_fields_ids = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]

        for field_id in valid_fields_ids:
            field = driver.find_element(By.ID, field_id)
            assert "alert-success" in field.get_attribute("class"), \
                f"Поле {field_id} не подсвечено зеленым, класс: {field.get_attribute('class')}"

    finally:
        driver.quit()
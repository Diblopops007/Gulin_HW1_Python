from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")


    start_url = driver.current_url


    driver.find_element(By.NAME, "custname").send_keys("Alex")


    driver.find_element(By.XPATH, "//button[text()='Submit']").click()


    assert driver.current_url != start_url

    driver.quit()
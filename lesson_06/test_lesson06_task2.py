from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)


    driver.get("https://gitflic.ru/")

    wait.until(EC.title_contains("GitFlic"))


    driver.add_cookie({
        "name": "SESSION",
        "value": "ZjA3OTE0MzYtM2I3NC00OWM3LWE4MzktNDE3YzI1M2MwOTBi",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })


    driver.refresh()

    wait.until(EC.title_contains("GitFlic"))


    driver.get("https://gitflic.ru/user/diblopops")

    wait.until(EC.url_contains("/user/diblopops"))

    wait.until(EC.text_to_be_present_in_element(
        (By.TAG_NAME, "body"), "diblopops"
    ))


    url_user1 = driver.current_url
    print(f"URL пользователя 1: {url_user1}")

    driver.delete_all_cookies()

    driver.get("https://gitflic.ru/")
    wait.until(EC.title_contains("GitFlic"))

    driver.add_cookie({
        "name": "SESSION",
        "value": "NDhkODdkZGMtMWFhNS00ODg2LWE2MTktODdiN2M4ZjYyZGMw",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()
    wait.until(EC.title_contains("GitFlic"))

    driver.get("https://gitflic.ru/user/diblopops007")
    wait.until(EC.url_contains("/user/diblopops007"))
    wait.until(EC.text_to_be_present_in_element(
        (By.TAG_NAME, "body"), "diblopops007"
    ))

    url_user2 = driver.current_url
    print(f"URL пользователя 2: {url_user2}")

    assert url_user1 != url_user2, \
        f"URL пользователей совпадают: {url_user1} == {url_user2}"

    print("Тест пройден: URL пользователей различаются.")

    driver.quit()
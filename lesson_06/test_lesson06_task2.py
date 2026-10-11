from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # 1. Открываем страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")
    sleep(2)

    # 2. Устанавливаем cookie пользователя 1
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

    # 3. Обновляем страницу
    driver.refresh()
    sleep(2)

    # 4. Переходим на страницу пользователя 1
    driver.get("https://gitflic.ru/user/diblopops")
    sleep(2)

    # 5. Сохраняем текущий URL
    url_user1 = driver.current_url
    print(f"URL пользователя 1: {url_user1}")

    # 6. Разлогиниваемся (очищаем куки)
    driver.delete_all_cookies()

    # 7. Обновляем страницу
    driver.refresh()
    sleep(2)

    # 8. Устанавливаем cookie пользователя 2
    driver.get("https://gitflic.ru/")
    sleep(2)
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

    # 9. Обновляем страницу
    driver.refresh()
    sleep(2)

    # 10. Переходим на страницу пользователя 2
    driver.get("https://gitflic.ru/user/diblopops007")
    sleep(2)

    # 11. Сохраняем текущий URL
    url_user2 = driver.current_url
    print(f"URL пользователя 2: {url_user2}")

    # 12. Проверяем, что URL различаются
    assert url_user1 != url_user2, \
        f"URL пользователей совпадают: {url_user1} == {url_user2}"

    print("Тест пройден: URL пользователей различаются.")

    driver.quit()
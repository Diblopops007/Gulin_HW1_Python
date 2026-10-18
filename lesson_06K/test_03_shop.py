from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_session_storage_auth():
    driver = webdriver.Firefox()
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        driver.find_element(By.ID, "checkout").click()
        
        driver.find_element(By.ID, "first-name").send_keys("Сергей")
        driver.find_element(By.ID, "last-name").send_keys("Гулин")
        driver.find_element(By.ID, "postal-code").send_keys("300010")
        
    
        driver.find_element(By.ID, "continue").click()
        
    
        total_element = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text 
       
        assert total_text == "Total: $58.29"
        
    finally:
        
        driver.quit()

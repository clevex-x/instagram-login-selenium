from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


driver_path = "chromedriver"

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:

    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5) 

    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("your_test_username")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("your_wrong_password")

    print("✅ Username and password entered (login not submitted).")

    time.sleep(2)
    driver.save_screenshot("instagram_login_demo.png")
    print("📸 Screenshot saved: instagram_login_demo.png")

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    time.sleep(2)
    driver.quit()

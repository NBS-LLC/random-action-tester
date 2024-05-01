from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
print(driver.title)

buttons = driver.find_elements(By.XPATH, '//input[@type="button"]')

for button in buttons:
    print(f"Clicking: {button.accessible_name}")
    button.click()

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By


def print_all_elements(driver: webdriver):
    for element in driver.find_elements(By.XPATH, "//*"):
        print(f"name: {element.accessible_name}")
        print(f"text: {element.text}")
        print(f'value: {element.get_attribute("value")}')
        print()


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
print(f"App Under Test: {driver.title}")
print()

print_all_elements(driver) # before

buttons = driver.find_elements(By.XPATH, '//input[@type="button"]')
for button in buttons:
    print(f"Clicking: {button.accessible_name}")
    button.click()
print()

print_all_elements(driver) # after

# TODO: diff the before and after, display only the differences

driver.quit()

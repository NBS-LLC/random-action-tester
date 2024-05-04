from textwrap import dedent

from deepdiff import DeepDiff
from selenium import webdriver
from selenium.webdriver.common.by import By


class Element:
    def __init__(self, name: str, text: str, value: str):
        self.name = name
        self.text = text
        self.value = value

    def __str__(self) -> str:
        return dedent(f"""
            name: {self.name}
            text: {self.text}
            value: {self.value}
        """).strip()


def get_all_elements(driver: webdriver.Remote):
    all_elements: list[Element] = []
    for element in driver.find_elements(By.XPATH, "//*"):
        all_elements.append(
            Element(
                element.accessible_name, element.text, element.get_attribute("value")
            )
        )
    return all_elements


def print_elements(elements: list[Element]):
    for element in elements:
        print(element)
        print()


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
print(f"App Under Test: {driver.title}")

before = get_all_elements(driver)
print(f"element count: {len(before)}")
print()

buttons = driver.find_elements(By.XPATH, '//input[@type="button"]')
for button in buttons:
    print(f"Clicking: {button.accessible_name}")
    button.click()
print()

after = get_all_elements(driver)
print(f"element count: {len(after)}")

print(DeepDiff(before, after).pretty())

driver.quit()

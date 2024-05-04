from textwrap import dedent

from deepdiff import DeepDiff
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


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

    def get_name(self) -> str:
        return self.name or self.text or self.value or "?"


def generate_xpath(child_element: WebElement, current: str):
    child_tag = child_element.tag_name
    if child_tag == "html":
        return "/html[1]" + current

    parent_element = child_element.find_element(By.XPATH, "..")
    children_elements = parent_element.find_elements(By.XPATH, "*")
    count = 0

    for _, children_element in enumerate(children_elements):
        children_tag = children_element.tag_name
        if child_tag == children_tag:
            count += 1
        if child_element == children_element:
            return generate_xpath(
                parent_element, "/" + child_tag + "[" + str(count) + "]" + current
            )

    return None


def get_all_elements(driver: webdriver.Remote):
    elements_by_name: dict[str, Element] = {}
    for web_element in driver.find_elements(By.XPATH, "//*"):
        element = Element(
            web_element.accessible_name,
            web_element.text,
            web_element.get_attribute("value") or "",
        )
        name = element.get_name()
        xpath = generate_xpath(web_element, "")
        elements_by_name[f"({name}){xpath}"] = element
    return elements_by_name


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

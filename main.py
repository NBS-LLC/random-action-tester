import random
import time
from textwrap import dedent

from deepdiff import DeepDiff
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Element:
    # TODO: might need to include computed values (css, etc)
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


def get_random_workflow(elements: list[WebElement], step_count: int, seed=1):
    random.seed(seed)
    return [random.choice(elements) for _ in range(step_count)]


WORKFLOW_COUNT = 3
STEP_COUNT = 10
END_GOAL = "Clicking: ="


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8080/")
print(f"App Under Test: {driver.title}")
print(f"Workflow Count: {WORKFLOW_COUNT}")
print(f"Step Count: {STEP_COUNT}")
print(f"End Goal: {END_GOAL}")
print()


for _ in range(WORKFLOW_COUNT):
    seed = int(time.time())

    driver.get("http://127.0.0.1:8080/")  # Reset to a clean app state
    buttons = driver.find_elements(By.XPATH, '//input[@type="button"]')
    workflow = get_random_workflow(buttons, STEP_COUNT, seed)
    print(f"Workflow Seed: {seed}")

    before = get_all_elements(driver)
    print(f"\tElement Count Before Workflow Run: {len(before)}")
    print()

    for element in workflow:
        step = f"Clicking: {element.accessible_name}"
        print("\t" + step)
        element.click()

        if step == END_GOAL:
            print("\tEnd Goal Reached")
            break
    print()

    after = get_all_elements(driver)
    print(f"\tElement Count After Workflow Run: {len(after)}")

    print("\t" + DeepDiff(before, after).pretty())
    print()

driver.quit()

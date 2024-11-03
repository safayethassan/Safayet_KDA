from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def perform_action(driver, keyword, element_xpath, timeout):
    driver.implicitly_wait(timeout)
    element = driver.find_element(By.XPATH, element_xpath)

    if keyword == "click":
        element.click()
    elif keyword == "input":
        value = input("Enter value: ")  # Modify to read from your Excel if needed
        element.send_keys(value)
    elif keyword == "navigate":
        driver.get(element_xpath)  # assuming the URL is passed as the xpath

    # Add more keywords as needed

def perform_assertion(driver, assertion_type, expected_value, actual_value, assertion_action):
    actual_value = driver.find_element(By.XPATH, actual_value).text
    if assertion_action == "equals":
        return actual_value == expected_value
    # Implement more assertion types as needed
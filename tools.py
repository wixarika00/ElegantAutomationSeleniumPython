from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")

print("I have arrived")
# WebDriverWait(driver, timeout: float, poll_frequency: float = 0.5,
WebDriverWait(browser, 10).until(alert_is_present())  # explicit wait
print("An alert appeared")
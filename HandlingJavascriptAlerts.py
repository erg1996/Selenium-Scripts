import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/javascript_alerts")

# For the JS Promt

AlertButton = browser.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")

AlertButton.click()

alert = browser.switch_to.alert

alert_text = alert.text

print(alert_text)

alert.accept()

time.sleep(5)

# For the JS input alert

InputAlert = browser.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")

InputAlert.click()

time.sleep(5)

Alert = browser.switch_to.alert

Alert.send_keys("Testing this alert")

Alert.accept()

time.sleep(5)

browser.quit()

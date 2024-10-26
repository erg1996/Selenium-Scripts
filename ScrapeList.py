""" go to the page about dog breeds. -https://seleniumplayground.practiceprobs.com/dogs/breeds/-
Click on the second tab (Table of Different Dog Breeds).
Click the column header for Country of Origin until the column is ascending.
Read out all the table data and write it into a nested Python list.
"""


import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://seleniumplayground.practiceprobs.com/dogs/breeds/")

table = browser.find_element(By.XPATH, "//label[@for='__tabbed_1_2']").click()

filter_table = browser.find_element(By.XPATH, "//th[normalize-space()='Country of Origin']").click()

TableData = []

table = browser.find_element(By.XPATH, "//tbody")

for tags in table.find_elements(By.XPATH, ".//td"):
    TableData.append(tags.text)

browser.quit()


for data in TableData:
    print(data)

#Testing explicit waits from https://www.hyrtutorials.com/p/waits-demo.html

from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.wait
from selenium.webdriver.support import wait
import selenium.webdriver.support.expected_conditions as EC

browser = webdriver.Firefox()
browser.get("https://www.hyrtutorials.com/p/waits-demo.html#google_vignette")
boton_textbox = browser.find_element(By.ID, "btn1")
boton_textbox.click()

espera = wait.WebDriverWait(browser,12)
espera.until(EC.element_to_be_clickable((By.ID, "txt1"))).send_keys("Hola mundo")

boton_textbox_10 = browser.find_element(By.ID, "btn2")
boton_textbox_10.click()


espera.until(EC.element_to_be_clickable((By.ID, "txt2"))).send_keys("Hola de nuevo")

browser.quit()

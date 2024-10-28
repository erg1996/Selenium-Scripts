#Script to login to the students portal and check the grades.

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://siaf.uma.edu.sv/uonline/login.aspx')
browser.maximize_window()
time.sleep(3)

user = ""
password = ""

boton_para_acceder = browser.find_element(By.ID, "estudiante").click()
time.sleep(1)
ingresar_usuario = browser.find_element(By.ID, "plogin_estudiante_UserName")
ingresar_password = browser.find_element(By.ID, "plogin_estudiante_Password")
time.sleep(1)
ingresar_usuario.send_keys(user)
ingresar_password.send_keys(password)
time.sleep(1)
boton_ingresar = browser.find_element(By.ID, "plogin_estudiante_LoginButton").click()
time.sleep(2)
browser.get("https://siaf.uma.edu.sv/uonline/portal_estudiante/notas_new.aspx")
time.sleep(2)
boton_notas_este_ciclo = browser.find_element(By.ID, "__tab_ctl00_ContentPlaceHolder1_tmenu_tnotas").click()
browser.get_full_page_screenshot_as_png()


time.sleep(3)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

openbrowers=webdriver.Chrome()
openbrowers.get("https://the-internet.herokuapp.com/login")
searchbox=openbrowers.find_element(By.ID,"username")
searchbox.send_keys("sufiyan")
searchbox=openbrowers.find_element(By.ID," tomsmith")
searchbox.send_keys("SuperSecretPassword!")
button = openbrowers.find_element(By.CSS_SELECTOR, "button.radius")
button.click()
time.sleep(7)
openbrowers.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

openbrowers=webdriver.Chrome()
openbrowers.get("https://www.google.com/")
searchbox=openbrowers.find_element(By.ID,"APjFqb")
searchbox.send_keys("datacamps")

time.sleep(3)
openbrowers.quit()
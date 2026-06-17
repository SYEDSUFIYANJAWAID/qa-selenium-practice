from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

openbrowers=webdriver.Chrome()
openbrowers.get("https://the-internet.herokuapp.com/checkboxes")
checkbox=openbrowers.find_element(By.XPATH,'(//*[@id="checkboxes"]/input[1]')
checkbox2=openbrowers.find_element(By.XPATH,'(//*[@id="checkboxes"]/input[2]')
checkbox2.click()
checkbox.click()
time.sleep(7)
openbrowers.quit()
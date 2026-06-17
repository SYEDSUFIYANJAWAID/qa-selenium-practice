from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

openbrower=webdriver.Chrome()
openbrower.get("https://www.google.com/")
searchbox=openbrower.find_element(By.NAME,"q")
textsearch=searchbox.send_keys("datacamps",Keys.RETURN)
time.sleep(7)
openbrower.quit()
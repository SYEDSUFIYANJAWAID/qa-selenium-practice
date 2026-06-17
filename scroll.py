from selenium import webdriver
from selenium.webdriver.common.by import By
import time

openbrowser = webdriver.Chrome()
openbrowser.get("https://the-internet.herokuapp.com/infinite_scroll")

openbrowser.execute_script("window.scrollTo(0, 1000)")
time.sleep(2)

openbrowser.execute_script("window.scrollTo(0, 2000)")
time.sleep(3)

openbrowser.execute_script("window.scrollTo(0, 10000)")
time.sleep(3)

openbrowser.quit()
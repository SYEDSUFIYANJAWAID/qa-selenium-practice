from selenium import webdriver
import time
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'pages'))
from login_page import login

openbrowers = webdriver.Chrome()
openbrowers.get("https://the-internet.herokuapp.com/login")
login1 = login(openbrowers)
login1.user_name("admin")
login1.password_type("admin")
login1.login_button_click()
time.sleep(3)
openbrowers.quit()
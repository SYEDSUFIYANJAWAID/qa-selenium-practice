from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class login:
    def __init__(self,openbrowers):
        self.openbrowers=openbrowers

    def user_name(self,user_name):
       self.openbrowers.find_element(By.ID, "username").send_keys(user_name)

    def password_type(self,password_type):
        self.openbrowers.find_element(By.ID,"password").send_keys(password_type)

    def login_button_click(self):
        self.openbrowers.find_element(By.CSS_SELECTOR, "button.radius").click()


openbrowers = webdriver.Chrome()
openbrowers.get("https://the-internet.herokuapp.com/login")
login1=login(openbrowers)
login1.user_name("sufiyan")
login1.password_type("1234")
login1.login_button_click()
time.sleep(3)
openbrowers.quit()
          
          
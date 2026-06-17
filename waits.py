# #  Implicit Wait
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# openbrowser=webdriver.Chrome()
# openbrowser.implicitly_wait(7)
# openbrowser.get("https://the-internet.herokuapp.com/dynamic_loading")
# openbrowser.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# button=openbrowser.find_element(By.XPATH,'//*[@id="start"]/button')
# button.click()
# button = openbrowser.find_element(By.ID, 'finish')
# print(button.text)
# time.sleep(10)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
openbrowser=webdriver.Chrome()
openbrowser.implicitly_wait(7)
openbrowser.get("https://the-internet.herokuapp.com/dynamic_loading")
openbrowser.get("https://the-internet.herokuapp.com/dynamic_loading/1")
button=openbrowser.find_element(By.XPATH,'//*[@id="start"]/button')
button.click()
wait = WebDriverWait(openbrowser, 10)
finish_element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
print(finish_element.text)
time.sleep(3)

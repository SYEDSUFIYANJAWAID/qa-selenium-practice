from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

openbrowser=webdriver.Chrome()
openbrowser.get("https://the-internet.herokuapp.com/javascript_alerts")
# button=openbrowser.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button')
# button.click()
# time.sleep(2)
# # Alert ko switch karo
# alert = openbrowser.switch_to.alert
# alert.send_keys("sufiyan")
# print(alert.text)   # alert ka message print karo
# alert.accept()       # "OK" click karna (alert band ho jayega)
# time.sleep(3)

button=openbrowser.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button')
button.click()
alert = openbrowser.switch_to.alert
alert.send_keys("Sufiyan")
time.sleep(2)   # popup ke input box mein type karna
alert.accept()                # OK click karna
result_text = openbrowser.find_element(By.ID, "result").text
print(result_text)
openbrowser.quit()
time.sleep(3)

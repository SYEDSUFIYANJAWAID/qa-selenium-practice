from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

openbrowser=webdriver.Chrome()
openbrowser.get("https://the-internet.herokuapp.com/dropdown")
dropdown=openbrowser.find_element(By.ID,"dropdown")
# dropdown.click()
# dropdown_select_option=openbrowser.find_element(By.XPATH,'//*[@id="dropdown"]/option[2]')
# dropdown_select_option.click()
# dropdown_select_option=openbrowser.find_element(By.XPATH,'//*[@id="dropdown"]/option[3]')
# dropdown_select_option.click()
dropdown_element = openbrowser.find_element(By.ID, "dropdown")
select = Select(dropdown_element)
select.select_by_visible_text("Option 1")
time.sleep(2)
select.select_by_visible_text("Option 2")
time.sleep(7)
openbrowser.quit()


#best option use this

# dropdown_element = openbrowser.find_element(By.ID, "dropdown")
# select = Select(dropdown_element)

# select.select_by_visible_text("Option 1")   # text se select
# # ya
# select.select_by_value("1")                  # value se select
# # ya
# select.select_by_index(1)                    # position se select

#Fayda: Click karne ki zaroorat nahi, seedha select ho jaata hai 
# chahe dropdown khula ho ya nahi.
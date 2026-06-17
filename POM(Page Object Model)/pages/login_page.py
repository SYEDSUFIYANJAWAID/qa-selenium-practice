from selenium.webdriver.common.by import By

class login:
    def __init__(self, openbrowers):
        self.openbrowers = openbrowers

    def user_name(self, user_name):
        self.openbrowers.find_element(By.ID, "username").send_keys(user_name)

    def password_type(self, password_type):
        self.openbrowers.find_element(By.ID, "password").send_keys(password_type)

    def login_button_click(self):
        self.openbrowers.find_element(By.CSS_SELECTOR, "button.radius").click()
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_field.clear()
        password_field.clear()
    
        if username != "":
            username_field.send_keys(username)
        if password != "":
            password_field.send_keys(password)
        
        login_button.click()

    def get_title(self):
        return self.driver.find_element(By.CLASS_NAME, "title").text
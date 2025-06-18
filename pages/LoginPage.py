from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.locate import LoginPageLocator
class LoginPage():
    def __init__(self, driver):
        self.roshan = driver
        self.lc=LoginPageLocator()

    def get_nav_login(self):
        return self.roshan.find_element(By.ID,self.lc.nav_login_id)
    def click_nav_login(self):
        self.get_nav_login().click()
    def get_uname_login(self):
        return self.roshan.find_element(By.ID,self.lc.uname_id)

    def enter_uname_login(self,username):
        self.get_uname_login().send_keys(username)
    def get_password_login(self):
        return self.roshan.find_element(By.ID, self.lc.pwd_id)
    def enter_password_login(self,password):
        self.get_password_login().sendkeys(password)
    def get_login_button(self):
        return self.roshan.find_element(By.XPATH, self.lc.button_xpath)

    def click_login_button(self):
        self.get_login_button().click()

    def login(self,username,password):
       # self.get_nav_login()
        self.click_nav_login()
        self.get_uname_login()
        self.enter_uname_login(username)
        self.get_password_login()
        self.enter_password_login(password)
        self.get_login_button()
        self.click_login_button()
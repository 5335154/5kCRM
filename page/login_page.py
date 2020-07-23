import time
from selenium.webdriver.common.by import By
from driver.browser import chrome_driver
from page.base_page import BasePage


class LoginCase(BasePage):
    def __init__(self):
        super().__init__()
        self.url = "http://localhost/index.php?m=user&a=login"
        #元素定位符
        self.locator_username = (By.NAME, 'name')
        self.locator_password = (By.NAME, 'password')
        self.locator_submit = (By.NAME, 'submit')

    def ele_username(self,username):
        self.driver.find_element(*self.locator_username).clear()
        self.driver.find_element(*self.locator_username).send_keys(username)

    def ele_password(self,password):
        self.driver.find_element(*self.locator_password).clear()
        self.driver.find_element(*self.locator_password).send_keys(password)

    def ele_submit(self):
        self.driver.find_element(*self.locator_submit).click()

    def login(self,username,password):
        self.open(self.url)
        self.ele_username(username)
        self.ele_password(password)
        self.ele_submit()
        time.sleep(2)
        shiji = BasePage.duanyan(self)
        self.quit()
        return shiji

    def login1(self,username,password):
        self.open(self.url)
        self.ele_username(username)
        self.ele_password(password)
        self.ele_submit()
        time.sleep(2)
        return self.driver

# lg = LoginCase()
# lg.login()
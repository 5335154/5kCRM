from selenium.webdriver.common.by import By
from driver.browser import chrome_driver


class BasePage():
    def __init__(self):
        self.driver = chrome_driver()

    def duanyan(self):
        shiti = self.driver.current_url
        return shiti

    def open(self,url):
        self.driver.get(url=url)

    def quit(self):
        self.driver.quit()



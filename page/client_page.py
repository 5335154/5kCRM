import time

from selenium.webdriver.common.by import By

from page.clue import Clue
from page.login import LogIn


class Client():
    '''添加客户'''
    def __init__(self,driver):
        self.driver=driver
    def click_client(self):
        self.driver.find_element(By.LINK_TEXT , "客户").click()
    def click_cat(self):
        self.driver.find_element(By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[1]').click()
    def click_new(self):
        self.driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div[1]/div/a').click()

    def send_name(self,name):
        self.driver.find_element(By.NAME,'name').send_keys(name)
    def company(self):
        self.driver.find_element(By.ID, 'ownership1').click()
    def click_save(self):
        self.driver.find_element(By.NAME,'submit').click()
    def click_owner(self):
        self.driver.find_element(By.ID,'owner_name').click()
    def select_owner(self):
        self.driver.find_element(By.XPATH, '//tbody[@id="d_content"]/tr[2]/td[1]/input').click()
        self.driver.find_element(By.XPATH,'/html/body/div[7]/div[3]/div/button[1]/span').click()
    def cat_client(self):
        '''查看客户信息'''
        self.click_client()
        time.sleep(2)
        self.driver.quit()
    def add_client(self, name):
        '''添加客户放入客户池'''
        self.click_client()
        self.click_new()
        self.send_name(name)
        self.company()
        time.sleep(2)
        self.click_save()
        return self.driver
    def add_client2(self,name):
        self.click_client()
        self.click_new()
        self.send_name(name)
        self.click_owner()
        self.select_owner()
        self.company()
        self.click_save()
# client = Client()
# client.add_client('dfajhfk')


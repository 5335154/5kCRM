import time

from selenium.webdriver.common.by import By

from page.login import LogIn


class Clue():
    def __init__(self):
        a = LogIn()
        self.driver = a.log_in('admin','banxian123')
    def click_clue(self):
        self.driver.find_element(By.LINK_TEXT,'线索').click()
    def click_new_clue(self):
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/a').click()
    def send_name(self,name):
        self.driver.find_element(By.ID, 'name').send_keys(name)
    def send_pname(self,pname):
        self.driver.find_element(By.ID, 'contacts_name').send_keys(pname)
    def click_save(self):
        self.driver.find_element(By.NAME, 'submit').click()
    def add_clue(self,name,pname):
        self.click_clue()
        self.click_new_clue()
        self.send_name(name)
        self.send_pname(pname)
        self.click_save()
        time.sleep(2)
        return self.driver
# b =Clue()
# b.add_clue('xhw','dengdeng')
class SwichToClient():
    def __init__(self):
        nc = Clue()
        self.driver=nc.add_clue('huwei','company')
    def clicl_switch(self):
        self.driver.find_element(By.LINK_TEXT, '转换').click()
    def click_name(self):
        self.driver.find_element(By.ID, 'name').click()
    def click_inclient(self):
        self.driver.find_element(By.ID, 'remove').click()
    def click_sava(self):
        self.driver.find_element(By.NAME, 'submit').click()
    def switchclient(self):
        self.clicl_switch()
        self.click_name()
        self.click_inclient()
        time.sleep(2)
        self.click_sava()
        return self.driver
# sc = SwichToClient()
# sc.switchclient()
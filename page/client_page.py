import time

from selenium.webdriver.common.by import By




class ClientPage():
    '''添加客户'''
    def __init__(self, driver):
        #/html/body/div[1]/div/div/div[2]/ul[1]/li[2]/a
        self.driver = driver
        self.locator_click_client = (By.LINK_TEXT, '客户')
        self.locator_click_cat = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[1]')
        self.locator_click_new = (By.PARTIAL_LINK_TEXT, '新建客户')
        self.locator_send_name = (By.NAME, 'name')
        self.locator_company = (By.ID, 'ownership1')
        self.locator_click_save = (By.NAME, 'submit')
        self.locator_click_owner = (By.ID, 'owner_name')
        self.locator_select_owner_click = (By.XPATH, '//tbody[@id="d_content"]/tr[2]/td[1]/input')
        self.locator_select_owner_choose = (By.XPATH, "/html/body/div[7]/div[3]/div/button[1]/span" )
        self.locator_reslut_catclient = (By.ID, 'share')
        self.locator_reslut_addclient  = (By.XPATH, '//div[@class="alert alert-success"]')
        self.locator_click_edit_client = (By.LINK_TEXT, '编辑')
        self.locator_send_newname = (By.NAME, 'name')
        self.locator_clicl_sava_edit = (By.NAME, 'submit')
        self.locator_assert_edit = (By.XPATH, '//div[@class="alert alert-success"]')
    def click_client(self):    #点击客户
        self.driver.find_element(*self.locator_click_client).click()

    def click_cat(self):       #点击查看
        self.driver.find_element(*self.locator_click_cat).click()

    def click_new(self):       #点击新建客户
        self.driver.find_element(*self.locator_click_new).click()

    def send_name(self,name):  #客户名称输入名字
        self.driver.find_element(*self.locator_send_name).send_keys(name)

    def company(self):         #选择公司性质
        self.driver.find_element(*self.locator_company).click()

    def click_save(self):      #点击保存
        self.driver.find_element(*self.locator_click_save).click()

    def click_owner(self):     #点击负责人
        self.driver.find_element(*self.locator_click_owner).click()

    def select_owner(self):    #选择负责人
        self.driver.find_element(*self.locator_select_owner_click).click()
        time.sleep(1)
        self.driver.find_element(*self.locator_select_owner_choose).click()

    def reslut_catclient(self):     #获取查看断言的文本信息
        res = self.driver.find_element(*self.locator_reslut_catclient).text
        return res

    def reslut_addclient(self):       #获取添加用户断言信息
        res1 = self.driver.find_element(*self.locator_reslut_addclient).text
        return res1

    def cat_client(self):      #获取添加用户不放入客户池的断言信息
        '''查看客户信息'''
        self.click_client()
        self.click_cat()
        res = self.reslut_catclient()
        return res

    def add_client(self, name, a =True):
        '''添加客户放入客户池,True表示选择负责人'''
        self.click_client()
        self.click_new()
        self.send_name(name)
        if a == 1 :
            self.click_owner()
            self.select_owner()
        self.company()
        time.sleep(2)
        self.click_save()
        res1 = self.reslut_addclient()
        return res1

    def click_edit_client(self):            #点击编辑客户
        self.driver.find_element(*self.locator_click_edit_client).click()

    def send_newname(self,newname):  #清除文本并将输入新信息
        self.driver.find_element(*self.locator_send_newname).clear()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(*self.locator_send_newname).send_keys(newname)

    def clicl_sava_edit(self):         #点击保存
        self.driver.find_element(*self.locator_clicl_sava_edit).click()

    def assert_edit(self):            #获取断言信息
        res4 = self.driver.find_element(*self.locator_assert_edit).text
        return res4

    def edit_client(self,newman):
        '''编辑客户'''
        self.click_client()
        self.click_edit_client()
        self.send_newname(newman)
        self.clicl_sava_edit()
        res4 = self.assert_edit()
        return res4









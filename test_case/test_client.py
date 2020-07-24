import time
import unittest
from driver.browser import chrome_driver
from page.client_page import ClientPage
from page.login_page import LoginCase


class ClientsTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()
        self.driver = driver
        li = LoginCase(self.driver)
        li.login("admin", "banxian123")

    def tearDown(self):
        self.driver.quit()
    def test_catclient(self):
        '''查看客户'''
        caclient =ClientPage(self.driver)
        res = caclient.cat_client()
        self.assertEqual("分享", res)
    def test_addclient_in(self):
        ''''添加客户放入客户池'''
        addclient  = ClientPage(self.driver)
        res1 = addclient.add_client("9537")
        self.assertIn("添加客户成功", res1)
    def test_addclient_notin(self):
        '''添加客户不放入客户池'''
        ac2 = ClientPage(self.driver)
        res2 = ac2.add_client("9538",1)
        self.assertIn("添加客户成功", res2)
    def test_edit_client(self):
        '''编辑客户'''
        vim = ClientPage(self.driver)
        res3 = vim.edit_client("9539")
        self.assertIn("客户编辑成功", res3)
    def test_flow_client(self):   #主流程
        ac2 = ClientPage(self.driver)
        res2 = ac2.add_client("9149")  #添加客户
        time.sleep(2)
        cc = ClientPage(self.driver)
        res = cc.cat_client()            #查看客户
        time.sleep(2)
        vim = ClientPage(self.driver)
        res3 = vim.edit_client("9159")     #编辑客户


if __name__ == '__main__':
    unittest.main()

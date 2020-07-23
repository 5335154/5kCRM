import unittest

from driver.browser import chrome_driver
from lib.data_lib import read_csv
from page.business_page import BusinessCase
from page.login_page import LoginCase


class BusinessTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_business(self):
        lg = LoginCase(self.driver)
        lg.login("admin","banxian123")
        bus = BusinessCase(self.driver)
        sj = read_csv(r"D:\git_root\5kCRM\data\business.csv")
        busname = sj[3][0]
        yprice = sj[3][1]
        shiji = bus.add_bus_opp(busname,yprice)

        self.assertIn("添加商机成功", shiji)


if __name__ == '__main__':
    unittest.main()

import unittest

from driver.browser import chrome_driver
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

        shiji = bus.add_bus_opp("王辉商机8号","10000")

        self.assertIn("添加商机成功", shiji)


if __name__ == '__main__':
    unittest.main()

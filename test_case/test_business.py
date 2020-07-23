import unittest

from driver.browser import chrome_driver
from page.business_page import BusinessCase


class BusinessTestCase(unittest.TestCase):
    def test_business(self):
        bus = BusinessCase()
        shiji = bus.add_bus_opp("王辉商机5号","10000")

        self.assertIn("添加商机成功", shiji)


if __name__ == '__main__':
    unittest.main()

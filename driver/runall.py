from HTMLTestRunner import HTMLTestRunner
import unittest

dicover = unittest.defaultTestLoader.discover('../test_case','test*py')
runner = unittest.TextTestRunner()
with open('report.html', 'wb') as f:
    runner = HTMLTestRunner(stream=f,
                            title='crm自动化测试',
                            description='运行环境 win10 chrome')
    runner.run(dicover)

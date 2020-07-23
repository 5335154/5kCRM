import unittest

from lib.data_lib import read_txt
from page.login_page import LoginCase


class LoginTestCase(unittest.TestCase):
    def test_login(self):
        lg = LoginCase()
        read = read_txt(r"D:\git_root\data\crmAuto41\data\user.txt")
        username = read[0][0]
        password = read[0][1]
        shiji = lg.login(username,password)

        self.assertEqual("http://localhost/index.php?m=dynamic&a=index", shiji)


if __name__ == '__main__':
    unittest.main()
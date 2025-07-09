import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from pages.LoginPage import LoginPage
from ddt import ddt,data,unpack
from utils.readdata import Read

@ddt()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.roshan = webdriver.ChromiumEdge()
        wait = WebDriverWait(self.roshan, 10)
        self.roshan.maximize_window()
        self.roshan.get("https://www.demoblaze.com")
        self.lp=LoginPage(self.roshan)
    def tearDown(self):
        self.tearDown()
        self.roshan.quit()

    @data(*Read.get_csv_data('../testdata/data.csv'))
    @unpack
    def test_a_login(self,username,password,case):

        self.lp.login(username,password)
        if case=='p':
            expected_result = True
            actual_result = True
            self.assertEqual(expected_result,actual_result)
        else:
            expected_result = "something went wrong"
            actual_result = "nothing went wrong"
            self.assertEqual(expected_result,actual_result)
        #self.lp.login("testmorning","password")


    def test_b_invalidpassword_login(self):
        self.lp.login("testmorning","invalidpassword")
        self.assertEqual(True,False,"hhh")
    def test_c_invalidusername_login(self):
        self.lp.login("invalidtestmorning","password")
        self.assertEqual(False,False,"False false")

if __name__ == '__main__':
    unittest.main()

#
#
# cart_button=driver.find_element(Byid,"")
# cart_button.click()
# cart_url="https://www.demoblaze.com/cart.html"
# current_url = driver.current_url
# self.assertEqual(cart_url,current_url,"The url is not correct")
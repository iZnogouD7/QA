import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        driver = webdriver.ChromiumEdge()
        driver.maximize_window()
        driver.get("https://www.demoblaze.com")

    def test_login(self,driver):
        nav_login = driver.find_element(By.ID, "login2")
        nav_login.click()
        uname = driver.find_element(By.ID, "loginusername")
        uname.send_keys("testmorning")
        username=driver.find_element(By.ID, "loginusername").text
        self.assertEqual(username, "testmorning","Invalid Username")

        expected_result="welcome testmorning"
        actual_result=driver.find_element(By.ID, "welcome").text
        self.assertEqual(expected_result,actual_result,"Invalid Username")

    def tearDownClass(self,driver):
        driver.quit()
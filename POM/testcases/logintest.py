import time

import HtmlTestRunner
import sys
import unittest
from selenium import webdriver
sys.path.append("/")
from POM.pages.loginpage import loginAutomation

def setUpModule():
    print("Connection establishing.....")
def tearDownModule():
    print("Connection closed.....")

class loginTest(unittest.TestCase):
    baseUrl ="https://practicetestautomation.com/practice-test-login/"
    valid_name = "student"
    valid_password = "Password123"
    invalid_name = "student1"
    invalid_password = "Password1234"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get(self.baseUrl)
        time.sleep(2)

    def test_Scenario1(self):
        TS1_login = loginAutomation(self.driver)
        TS1_login.test_login(self.valid_name,self.valid_password)
        self.assertEqual(self.driver.title,"Logged In Successfully | Practice Test Automation")

    def test_Scenario2(self):
        TS2_login = loginAutomation(self.driver)
        TS2_login.test_login(self.invalid_name,self.valid_password)
        self.assertEqual(self.driver.title,"Logged In Successfully | Practice Test Automation")

    def test_Scenario3(self):
        ts3_login = loginAutomation(self.driver)
        ts3_login.test_login(self.valid_name,self.invalid_password)
        self.assertEqual(self.driver.title,"Logged In Successfully | Practice Test Automation")

    def tearDown(self):
        logout = loginAutomation(self.driver)
        logout.test_logout()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C://Users/Admin/PycharmProjects/practiceTestAutomation/POM/reports'))
from selenium.webdriver.common.by import By

class loginAutomation:
    ele_name = "username"
    ele_password = "password"
    ele_login = "submit"
    ele_logout = "//a[.='Log out']"

    def __init__(self,driver):
        self.driver=driver

    def test_login(self,valid_name,valid_password):
        self.driver.find_element(By.ID,self.ele_name).send_keys(valid_name)
        self.driver.find_element(By.ID,self.ele_password).send_keys(valid_password)
        self.driver.find_element(By.ID,self.ele_login).click()

    def test_title(self):
            self.driver.title

    def test_logout(self):
        self.driver.find_element(By.XPATH,self.ele_logout).click()
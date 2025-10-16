import time
from selenium.webdriver.common.by import By

class CommonCode:
    def __init__(self, driver,username,password):
        self.driver = driver
        self.password=password
        self.username=username
        pass
    def login_check(self):
        self.driver.find_element(By.NAME,"username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.ID,"submit").click()
        time.sleep(3)
        print(self.driver.title)
        print("login successfull")
        assert self.driver.title=="Logged In Successfully | Practice Test Automation"    
        
    def invild_check(self):
        self.driver.find_element(By.NAME,"username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.ID,"submit").click()
        time.sleep(3)
        assert self.driver.title!="Logged In Successfully | Practice Test Automation"
    
       
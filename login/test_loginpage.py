# from login.common_logic import CommonCode


import time
from .common_logic import CommonCode
from selenium.webdriver.common.by import By

def test_login(setup_driver):
    driver = setup_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    obj=CommonCode(driver,"student","Password123")
    obj.login_check()
    
    driver.find_element(By.CLASS_NAME,"wp-block-button__link").click()

    obj1=CommonCode(driver,"alokkk","riytte34343")
    obj1.invild_check()
    
    # driver.find_element(By.NAME,"username").send_keys("student")
    # driver.find_element(By.NAME, "password").send_keys("Password1234")
    # driver.find_element(By.ID,"submit").click()
    # time.sleep(5)
    # tab=driver.title
    # print(driver.title)

    # assert tab=="Logged In Successfully | Practice Test Automation"



   


    

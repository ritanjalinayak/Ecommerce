
import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def setup_driver():
    print("fixture started")
    driver = webdriver.Chrome()
    time.sleep(3)
    yield driver
    time.sleep(4)
    print("login test has been done ")
    # time.sleep(3)
    driver.quit()
    
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.ui import Select
#driver = webdriver.Chrome()
#driver.get('http://192.168.48.221:8001/')
#driver.maximize_window()
#driver.get_screenshot_as_file()
#time.sleep(3.0)

n = 63

for i in range(1, 7):
    res = pow(n, 1/i)
    if res == 2:
        print(n, i)
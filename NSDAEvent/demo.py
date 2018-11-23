from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.touch_actions import TouchActions

driver = webdriver.Chrome()
driver.get('http://192.168.48.221:8001/')
print(driver.maximize_window())


time.sleep(3.0)

if '关于我们' in driver.page_source:
    print('yes')
else:
    print('else')

driver.f
time.sleep(3.0)


driver.close()


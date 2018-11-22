from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.touch_actions import TouchActions

driver = webdriver.Chrome()
driver.get('http://192.168.48.221:8001/eventmanage/eventmanage/cyclingsetting/45')
print(driver.maximize_window())


time.sleep(3.0)



action = webdriver.TouchActions(driver)
action.scroll(100, 200).perform()
time.sleep(3.0)
driver.find_element_by_xpath()
driver.close()


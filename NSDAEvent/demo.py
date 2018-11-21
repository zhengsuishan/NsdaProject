from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get('http://192.168.48.221:8001/eventmanage/eventmanage/cyclingsetting/45')
print(driver.maximize_window())


time.sleep(3.0)

driver.find_element(By.XPATH, '//*[@id="dataHead"]/ul[2]/li/a[1]').click()
time.sleep(3.0)

driver.switch_to.frame('fg-layer-iframe1')
driver.find_element_by_xpath('//*[@id="playeremail"]').send_keys('haha')
time.sleep(1.0)

driver.close()


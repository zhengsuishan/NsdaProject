from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get('http://192.168.48.221:8001/')
driver.maximize_window()
time.sleep(3.0)

driver.find_element_by_xpath('//*[@id="dataHead"]/ul[2]/li/a[2]').click()
time.sleep(1.0)
driver.switch_to.frame('fg-layer-iframe1')
driver.find_element_by_xpath('//*[@id="txtAccount"]').send_keys('875707618@qq.com')
time.sleep(20)
driver.find_element_by_xpath('//*[@id="txtPwd"]').send_keys('test1234')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="txtPwd1"]').send_keys('test1234')
driver.find_element_by_xpath('//*[@id="btn_register"]').click()
driver.find_element_by_xpath('//*[@id="btn_register"]').click()
driver.find_element_by_xpath('//*[@id="btn_register"]').click()
driver.find_element_by_xpath('//*[@id="btn_register"]').click()



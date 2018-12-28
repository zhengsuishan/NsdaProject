# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

url = 'http://www.tongxiao.com.cn/Html/JiShuqqQun_558/#957'
net_wait_time = 15
import time

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    WebDriverWait(driver, net_wait_time).until(lambda driver:driver.find_element_by_xpath('/html/body/div[1]/div[2]/li[2]/a'))

    for i in range(0, 1000):
        string_cmd = '/html/body/div[1]/div[2]/li["%d"]/a'%(i+1)
        print(string_cmd)
        driver.find_element_by_xpath(string_cmd).click()
        time.sleep(3.0)

        driver.switch_to.window(driver.window_handles[1])

        text = driver.find_element_by_xpath('//*[@id="body"]/table/tbody/tr/td/table/tbody/tr[4]/td[2]/font').text
        text = text.replace('\n', '')
        text = text.strip()
        file = open('qun_num', 'a+')

        file.write('\n')
        file.write(text)

        file.close()

        driver.switch_to.window(driver.window_handles[0])
        WebDriverWait(driver, net_wait_time).until(
            lambda driver: driver.find_element_by_xpath('/html/body/div[1]/div[2]/li[2]/a'))





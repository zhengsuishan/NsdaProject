from appium import webdriver

desired_cups = {}

desired_cups['platformName'] = 'Android'

desired_cups['platformVersion'] = '5.0.2'

desired_cups['deviceName'] = 'HuaWei'

desired_cups['appPackage'] = 'com.grandsoft.intercom'

desired_cups['appActivity'] = 'com.grandsoft.intercom.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_cups)

driver.find_element_by_name('').clear()
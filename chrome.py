from selenium import webdriver
driver=webdriver.Chrome('chromedriver_linux64/chromedriver')
driver.get('http://www.google.com')
driver.maximize_window()
finder=driver.find_element_by_xpath('//input[@name="q"]')
finder.send_keys('how to erase my hard disk in dell laptop')
finder.submit()
driver.quit()
from selenium import webdriver
#pip install selenium
import time
import sqlite3 as sq
#download chrome web driver and add it to path
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()
# I am using chrome for this
driver.get('https://www.linkedin.com/uas/login')
#opens the site in a new browser window
#this time mentioned is for the user to see and login
time.sleep(25)
#Woring on searching
text_area = driver.find_element_by_xpath('//*[@id="ember41"]/input')
text_area.send_keys("Amitab Bachan")
driver.quit()

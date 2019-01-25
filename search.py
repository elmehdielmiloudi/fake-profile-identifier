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
#this time mentioned is for the user to see
text_area = driver.find_element_by_id('username')
#finding where to fill the text
#sendig the text to be filled
text_area.send_keys("username")
text_area = driver.find_element_by_id('password')
text_area.send_keys("password")
# click submit button
submit_button = driver.find_elements_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')[0]
#login button
submit_button.click()
#clicks it
#find search box
search=driver.find_element_by_xpath("//*[@id=\"ember36\"]/input")
search.send_keys("Amitab Bachan","\n")
#enter the entity name to search
#Now it loads popular profile results all we need is to collect the profile links
str=[]
#collects profile links
for a in driver.find_elements_by_xpath('.//a'):
    if a.get_attribute("data-control-name")==("search_srp_result"):
        if a.get_attribute("class")==("search-result__result-link search-result__result-link--visited ember-view"):
            str.append(a.get_attribute("href"))
#these if statements are for getting exact links to the resultant profiles










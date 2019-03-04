from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/uas/login')
text_area = driver.find_element_by_id('username')
text_area.send_keys("theunmountedprogrammer@gmail.com")
text_area = driver.find_element_by_id('password')
text_area.send_keys("theunmountedprogrammer@31")
submit_button = driver.find_elements_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')[0]
submit_button.click()
s=[]
s=["Amitab Bachan","Samantha","Mark Zuckerberg"]
l=(len(s))
def search(m):
    driver.get("https://www.linkedin.com/feed/")
    search=driver.find_element_by_xpath("//*[@id=\"ember30\"]/input")
    search.send_keys(m,"\n")
    time.sleep(5)
    print("Seraching profiles with the name",m)
    res=[]
    for a in driver.find_elements_by_xpath('.//a'):
        res.append(a.get_attribute("href"))
    n=""
    n=m.lower()
    n=n.replace(" ","-")
    for i in range (len(res)):
        if n in res[i]:
          print(res[i])
for i in range(len(s)):
    z=s[i]
    search(z)


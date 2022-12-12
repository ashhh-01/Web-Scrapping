#Amazon Scrapping
# from selenium import webdriver 
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# service=Service("D:\software\Selentium\chromedriver\chromedriver.exe")
# driver=webdriver.Chrome(service=service)
# driver.get("https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/")
 
# # price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# # print(price.get_attribute('innerHTML')) 

# searchbar=driver.find_element(By.NAME,"field-keywords")
# # print(searchbar.tag_name)

# link=driver.find_element(By.XPATH,'//*[@id="nav-logo-sprites"]')
# print(link.get_attribute("innerHTML"))


#
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service("D:\software\Selentium\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.python.org/")

event_time=driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_names=driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
events={}

for n in range(0,len(event_time)):
    events[n]={
        "time":event_time[n].text,
        "name":event_names[n].text
    }
print(events[0])
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.keys import Keys

# service=Service("D:\software\Selentium\chromedriver\chromedriver.exe")
# driver=webdriver.Chrome(service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count=driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
# # print(article_count.text)
# # article_count.click()

# allportals=driver.find_element(By.LINK_TEXT,"Elden Ring")
# # allportals.click()

# search=driver.find_element(By.NAME,"search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# time.sleep(5)


###Challenge



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

service=Service("D:\software\Selentium\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("http://secure-retreat-92358.herokuapp.com/")

form=driver.find_element(By.NAME,"fname")
form.send_keys("Ash"+Keys.TAB+"Ash"+Keys.TAB+"Ash@gmail.com")
button=driver.find_element(By.CSS_SELECTOR,"form button")
button.click()
time.sleep(5)
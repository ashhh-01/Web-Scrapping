from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service=Service("D:\software\Selentium\chromedriver\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie=driver.find_element(By.ID,"cookie")
items=driver.find_elements(By.CSS_SELECTOR,"#store div")
item_id=[id.get_attribute("id") for id in items]
item_id.pop()

time_to_buy=time.time()+10
stop_time=time.time()+60*5
game_is_on=True
while game_is_on:
   cookie.click()
   if time.time()>time_to_buy:
    to_buy_index=0
    money=int(driver.find_element(By.ID,"money").text.replace(",",""))  
    prices=driver.find_elements(By.CSS_SELECTOR,"#store b")
    prices.pop()
    price_list=[int(price.text.replace(" ","").split("-")[1].replace(",","")) for price in prices]
    for price in price_list:
        if money>price:
            to_buy_index=price_list.index(price)
        item_to_buy=driver.find_element(By.ID,item_id[to_buy_index])
        item_to_buy.click()
        time_to_buy=time.time()+10
    if time.time()>stop_time:
        cps=driver.find_element(By.ID,"cps").text
        print(cps)
        game_is_on=False

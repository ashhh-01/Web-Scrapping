PROMISED_DOWN=50
PROMISED_UP=30
EXC_PATH="D:\software\Selentium\chromedriver\chromedriver.exe"
EMAIL="XYZ@gmail.com"
PASSWORD="asdfghjkl"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver=webdriver.Chrome(service=Service(EXC_PATH))
        self.up=0
        self.down=0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        time.sleep(3)
        start.click()
        time.sleep(50)
        self.down=float(self.driver.find_element(By.CSS_SELECTOR,"span.download-speed"))
        self.up=float(self.driver.find_element(By.CSS_SELECTOR,"span.upload-speed"))
    
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/signup")
        time.sleep(3)
        ##Login
        login=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[7]/span[2]')
        login.click()
        time.sleep(3)
        email=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.click()
        email.send_keys(EMAIL+Keys.ENTER+PASSWORD+Keys.ENTER)
        time.sleep(10)
        ##Tweet
        tweetlink=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweetbox=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweetlink.click()
        time.sleep(5)
        TWEET=f"Internet download speed {self.up} and download speed {self.down}"
        tweetbox.send_keys(TWEET)
        time.sleep(10)
        sendtweet=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div')
        sendtweet.click()
        time.sleep(2)
        self.driver.quit()



bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.up<PROMISED_UP and bot.down<PROMISED_DOWN:
    bot.tweet_at_provider()
    
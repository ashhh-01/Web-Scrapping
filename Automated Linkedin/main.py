from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,os
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains


service=Service("D:\software\Selentium\chromedriver\chromedriver.exe")
drive=webdriver.Chrome(service=service)
drive.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

load_dotenv("../../../Python/Python/Python Env/env")

EMAIL=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD")

loginpage=drive.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[1]")
loginpage.click()
signin=drive.find_element(By.XPATH,"/html/body/div[1]/main/p[1]/a")
signin.click()
email=drive.find_element(By.NAME,"session_key")
email.click()
email.send_keys(EMAIL+Keys.TAB+PASSWORD)
login=drive.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
login.click()
time.sleep(3)

alllist=drive.find_elements(By.XPATH,'//*[@id="main"]/div/section[1]/div/ul')
for list in alllist:
    lists=list.find_elements(By.CLASS_NAME,"job-card-list__title")
    for indilist in lists:
        indilist.click()
        time.sleep(3)
        #Applying for the job
        # try:
        #     easyapply=drive.find_element(By.CLASS_NAME,"jobs-apply-button")
        #     easyapply.click()
        #     drive.implicitly_wait(10)
        #     # # nextstep=drive.find_elements(By.CSS_SELECTOR,".artdeco-button--2 button")
        #     # nextstep=drive.find_element(By.XPATH,'//*[@id="ember418"]')
        #     # # nextstep.click()
        #     # drive.implicitly_wait(10)
        #     # ActionChains(drive).move_to_element(nextstep).click(nextstep).perform()
        # except:
        #     continue

        ##Save Jobs
        jobsave=drive.find_element(By.CLASS_NAME,"jobs-save-button")
        jobsave.click()
time.sleep(3)




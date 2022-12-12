import requests
from bs4 import BeautifulSoup
import lxml,smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

URL="https://www.amazon.com/dp/B0B4MYBLZQ/ref=syn_sd_onsite_desktop_97?ie=UTF8&pd_rd_plhdr=t&th=1"

header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}
response=requests.get(URL,headers=header)

soup=BeautifulSoup(response.text,"lxml")
##Price##
price=soup.find(name="span",class_="a-offscreen").getText()
price_without_currency=price.split("$")[1]
price_as_float=float(price_without_currency)

##Product Name##

product_name=soup.find(name="span",id="productTitle").getText().strip()

load_dotenv("../../../Python/Python/Python Env/env")

BUY_PRICE=120
MY_EMAIL=os.getenv("MY_EMAIL")
PASSWORD=os.getenv("MY_PASSWORD")
message=f"The price of the product {product_name} is at a low price of {price_as_float}"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(EMAIL,PASSWORD)
#     connection.sendmail(
#         to_addrs=EMAIL,
#         from_addr=EMAIL,
#         msg=f"Subject:Amazon Price Drop\n\n {message}\n\n{URL}".encode("ascii",errors="ignore")
#     )

def send_email(address, message):
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
 
    email_message = EmailMessage()
    recipient_address = address
    sender_address = MY_EMAIL
    subject = "Amazon Price Alert!"
 
    fmt = "From: {}\r\nTo: {}\r\nSubject: {}\r\n{}"
    email_message.set_content(fmt.format(recipient_address, sender_address, subject, message))
    email_message['To'] = recipient_address
    email_message['From'] = sender_address
    email_message['Subject'] = subject
 
    connection.send_message(email_message)
    connection.close()
send_email(MY_EMAIL, message)
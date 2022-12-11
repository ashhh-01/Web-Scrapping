
# from bs4 import BeautifulSoup
# with open("./bs4-start/website.html", encoding="utf-8") as file:
#     contents = file.read()
 
# soup = BeautifulSoup(contents, "html.parser")
# # all=soup.find_all(name="a")
# # for tag in all:
# #     print(tag.get("href"))

# heading=soup.find(name="h1",id="name")
# print(heading)

import requests
from bs4 import BeautifulSoup
response=requests.get("https://news.ycombinator.com/newest")
vc_web_page=response.text

soup=BeautifulSoup(vc_web_page,"html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts=[]
article_links=[]
for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.find(name="a").get("href")
    article_links.append(link)
    article_texts.append(text)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
 
largest_number= max(article_upvote)
largest_index=article_upvote.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
# print(article_texts)
# print(article_links)
# print(article_upvote)

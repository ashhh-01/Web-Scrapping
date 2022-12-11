import requests
from bs4 import BeautifulSoup

URL="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(URL)
contents=response.text
soup=BeautifulSoup(contents,"html.parser")
allMovie=soup.find_all(name="h3",class_="title")

movie_titles=[names.getText() for names in allMovie]
Movies=movie_titles[::-1]

with open("./Projects/Top100Movies/movies.txt",mode="w",encoding="utf-8") as file:
    for movie in Movies:
        file.write(f"{movie}\n")
from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
respond = requests.get(url)
movie_web_page = respond.text

soup = BeautifulSoup(movie_web_page, "html.parser")

names_tag = soup.find_all(name="h3", class_="title")
movie_title = [name.getText() for name in names_tag]
movies = movie_title[::-1]

with open("Movie to Watch", mode="w",  encoding="utf8") as file:
    for name in movies:
        file.write(f"{name}\n")
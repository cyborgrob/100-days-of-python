from bs4 import BeautifulSoup
import requests


# Gets HTML from website
resp = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
empire_html = resp.text

# Creates Soup object with HTML text, finds all movie title instances
soup = BeautifulSoup(empire_html, 'html.parser')
movies = soup.find_all('h3', class_='listicleItem_listicle-item__title__hW_Kn')

# Creates list of movies
movie_list = [movie.getText() for movie in movies]

movie_list.reverse()

# Writes list of movies to new .txt file
with open("movies.txt", "w") as file:
    for movie in movie_list:
        file.write(movie + "\n")

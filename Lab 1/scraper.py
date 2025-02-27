import requests
from bs4 import BeautifulSoup
import csv

def get_movies(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    # print(soup.prettify())
    movies = soup.find_all('li', {"class":'ipc-metadata-list-summary-item'})
    # print(movies[0])
    print(len(movies))
    titles = [movie.h3.text.split(". ")[1] for movie in movies]
    # print(titles)
    rankings = [movie.h3.text.split(". ")[0] for movie in movies]
    # print(rankings)
    years = [movie.find_all('span')[1].text for movie in movies]
    # print(years)
    ratings = [movie.find_all('span')[4].span.text.split("\xa0")[0] for movie in movies]
    # print(ratings)
    lst = list(zip(titles, rankings, years, ratings))
    lst = [list(elem) for elem in lst]
    
    str_lst = [f"{lst[i][1]} / {lst[i][0]} ({lst[i][2]}) / Starring: {lst[i][3]}" for i, val in enumerate(lst)]
    
    res = [elem.split('/') for elem in str_lst]
    
    with open("imdb_top_250.csv", "w") as f:
        writer = csv.writer(f, delimiter="-")
        writer.writerows(res)
        
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
url = "http://www.imdb.com/chart/top/"
get_movies(url)

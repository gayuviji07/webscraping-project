import requests
import csv
from bs4 import BeautifulSoup

headers = {"user-Agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebkit/537.36(KHTML,like Geocko) Chrome/58.0.3029.110 Safari/537.3"}
response = requests.get("https://www.imdb.com/chart/top",headers=headers)
#print(response)
soup = BeautifulSoup(response.text,"html.parser")
#print(soup)
content = soup.find('ul', class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 iyTDQy compact-list-view ipc-metadata-list--base')
#print(content)
movies = content.find_all('li')
#print(movies)
#using loop function
#csv file

with open('movie.csv',mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['moviename', 'year', 'duration','rating'])
    
    for movie in movies:
        movie_name = movie.find('h3').text.strip()
        moviename = movie_name[3:]
        print("name of the movie:  ",moviename)
        

        year_and_duration = movie.find('div', class_="sc-300a8231-6 dBUjvq cli-title-metadata").text

        #print(year_and_duration)
        year = year_and_duration[0:4]
        print("year of movie is:",year)
        duration = year_and_duration[4:10]
        print("movie duration: ",duration)
        ratings = movie.find('div', class_='sc-e2dbc1a3-0 jeHPdh sc-300a8231-3 koIPa cli-ratings-container').text
        rating =ratings[0:3]
        print("Ratings: ", rating)


        writer.writerow([moviename, year, duration,rating])
        print("----------------------------------------------------------------------------")
        






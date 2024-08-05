from bs4 import BeautifulSoup
import requests, os

def get_top_movies():
    titles = []
    years = []
    ratings = []
    website = "https://www.imdb.com/chart/top/"
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'} # creating the headers is a must in order to avoid getting 403 as response, we are mymi
    try:
        result = requests.get(website, headers=HEADERS)
        if result.status_code == 200:
            content = result.text
            soup = BeautifulSoup(content, "lxml")
            box = soup.find("div", class_="sc-c8984160-3 jAYdME ipc-page-grid__item ipc-page-grid__item--span-2") # the part where the name of the movies are situated
            movie_selector = box.find_all("li", class_="ipc-metadata-list-summary-item sc-10233bc-0 TwzGn cli-parent") # extracting every movie
            for movie in movie_selector:
                title = movie.find("h3", class_="ipc-title__text") # extracting the title of the movie is situated in a header
                year = movie.find("span", class_="sc-b189961a-8 hCbzGp cli-title-metadata-item") # extracting the year of the selected movie
                rating = movie.find("span", class_="ipc-rating-star--rating") # extracting the rating of the selected movie
                if title and year and rating:
                    titles.append(title.text)
                    years.append(year.text)
                    ratings.append(rating.text) 
            output_path = os.path.join('data', 'movies.txt')                         
            with open(output_path, "w", encoding="utf-8") as f:
                for title, year, rating in zip(titles, years, ratings):
                    f.write(title + f" released in {year}" +  f" rated as {rating}" + "\n")
        else:
            print(f"We have failed to retrieve the page. The status code that has been received is: {result.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


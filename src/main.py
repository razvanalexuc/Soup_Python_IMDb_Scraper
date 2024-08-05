from soupscraper import get_top_movies
import sys

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8') # sys was used for this encoding conversion due to the title of the movies being in Romanian and containing diacritics (my case scenario)
    get_top_movies()
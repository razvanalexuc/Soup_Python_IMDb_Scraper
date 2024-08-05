# Soup Python IMDb Scraper

This project is a Python script that scrapes the top 250 movies from the IMDb website and saves the movie titles, release years, and ratings to a file. It is my first take on learning how to use Beautiful Soup for Web Scraping pages that are using HTML and CSS.

## Features

- Scrapes the top 250 movies from IMDb
- Extracts movie titles, release years, and ratings
- Saves the extracted data to a `movies.txt` file in the `data` directory

## Requirements

- Python 3.x
- BeautifulSoup4
- Requests
- lxml

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/razvanalexuc/soup-python-imdb-scraper.git
   cd soup-python-imdb-scraper

2. Create and activate a virtual environment

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate

3. Install the required packages: 

   pip install -r requirements.txt

## Usage

1. Run the script:

   python src/main.py

2. The output file movies.txt will be generated in the data directory.

## Notes

1. Ensure you have a stable internet connection while running the script.
2. The script mimics a browser request to avoid getting blocked by IMDb.

## License

This project is licensed under the MIT License.
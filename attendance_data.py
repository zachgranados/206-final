import sqlite3
import requests
from bs4 import BeautifulSoup
import os


# web scrape from the url 
def scrape_website(url):
    # Send a GET request to the URL
    url = 'https://www.d1ticker.com/2023-fbs-attendance-trends/'

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text 
    else: 
        print("failed to retrieve the web page.")

    soup = BeautifulSoup(html, 'html.parser')
    
    
    






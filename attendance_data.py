import sqlite3
import requests
from bs4 import BeautifulSoup
import os


# web scrape from the url 
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the elements containing the data you want to scrape
        # For example, scrape all <th> tags with class "column..."
        schools = soup.find_all('th', class_='column-3 sorting') #need to change the tag and class for the right data
        
        # Extract the text from each table header and store it in a list
        content = [school.text.strip() for school in schools]
        
        return content
    else:
        print('Failed to retrieve webpage:', response.status_code)
        return []
    
url = 'https://www.d1ticker.com/2023-fbs-attendance-trends/'
content = scrape_website(url)
for school in content:
    print(school)





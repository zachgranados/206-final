import sqlite3
import requests
from bs4 import BeautifulSoup
import os


# web scrape from the url 
def get_website(url):
    # Send a GET request to the URL
    url = 'https://www.d1ticker.com/2023-fbs-attendance-trends/'

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text 
    else: 
        print("failed to retrieve the web page.")

    soup = BeautifulSoup(html, 'html.parser')

    get_school_data(soup)


# get the school and the average 2023 average attendance
import requests
from bs4 import BeautifulSoup

def get_school_data(soup):
    table = soup.find('table', class_='tablepress')
    if table:
        data = table.find_all('tr')
        current_average = {}
        for index in range(1, len(data)): 
            cells = data[index].find_all('td')
            if len(cells) >= 2:
                school_name = cells[0].text.strip()
                average_attendance_str = cells[1].text.strip().replace(',', '')
                try:
                    average_attendance = int(average_attendance_str)
                    current_average[school_name] = average_attendance
                except ValueError:
                    print(f"Skipping non-numeric value for school: {school_name}")
        return current_average
    else:
        print("Table not found.")
        return None






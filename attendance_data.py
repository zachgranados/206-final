import requests
from bs4 import BeautifulSoup
import sqlite3

def create_database():
    conn = sqlite3.connect('attendance_data.db')
    c = conn.cursor()
    
    # Create the table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS AttendanceData
                 (School TEXT, 
                 '2023 Average' INTEGER, 
                 '2022 Average' INTEGER, 
                 'Percentage Change' REAL)''')
    
    conn.commit()
    conn.close()

def scrape_data():
    url = 'https://www.d1ticker.com/2023-fbs-attendance-trends/'
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', class_='tablepress')
        if table:
            data = table.find_all('tr')
            
            school_data = {}
            for row in data:
                cells = row.find_all('td')
                if len(cells) >= 4:
                    school_name = cells[0].text.strip()
                    avg_2023 = cells[2].text.strip()  # Adjust index to get 2023 average
                    avg_2022 = cells[3].text.strip()  # Previous index for 2022 average
                    percentage_change = cells[4].text.strip()
                    school_data[school_name] = {
                        '2023_average': avg_2023,
                        '2022_average': avg_2022,
                        'percentage_change': percentage_change
                    }
            
            return school_data
        else:
            print("Table not found on the webpage.")
            return None
    else:
        print("Failed to retrieve the webpage.")
        return None


def insert_data(school_data):
    conn = sqlite3.connect('attendance_data.db')
    c = conn.cursor()
    c.execute('''DELETE FROM AttendanceData''')   
    # Insert data into the table
    for school, data in school_data.items():
        c.execute("INSERT INTO AttendanceData (School, '2023 Average', '2022 Average', 'Percentage Change') VALUES (?, ?, ?, ?)",
                  (school, data['2023_average'], data['2022_average'], data['percentage_change']))
        print(f"Inserted data for {school}")
        
    conn.commit()
    conn.close()

def main():
    create_database()
    data = scrape_data()
    if data:
        insert_data(data)
        print("Data inserted successfully.")
    else:
        print("No data available.")

if __name__ == "__main__":
    main()

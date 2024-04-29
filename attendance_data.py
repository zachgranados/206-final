import requests
from bs4 import BeautifulSoup
import sqlite3
   
# gets the needed data 
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


def insert_25_attendance(school_data, cur, conn):
    # school_data is a dict with school name as its title 

    #tracks number of schools added
    count = 0

    # schools = key so it is the string of the school name
    for schools in school_data:
        if count < 25:
            # get id from teams table given school

            # handles exceptions with formatting etcs
            if schools == "Army West Point":
                team = "Army"
            elif schools == "ECU":
                team = "East Carolina"
            elif schools == "FIU":
                team = "Florida International"
            elif schools == "Miami (FL)":
                team = "Miami"
            elif schools == "UConn":
                team = "Connecticut"
            elif schools == "UTSA":
                team = "UT San Antonio"
            elif schools == "Hawaii":
                team = "Hawai'i"
            elif schools == "Louisiana–Monroe":
                team = "Louisiana Monroe"
            elif schools == "Massachusetts":
                team = "UMass"
            elif schools == "San Jose State":
                team = "San José State"
            elif schools == "Southern Miss":
                team = "Southern Mississippi"
            else:
                team = schools
            
            #print(team)
            cur.execute("SELECT team_id FROM teams WHERE school = ?", (team,))
            team_id = cur.fetchall()[0][0]

            # verify if this team has been added before
            cur.execute("SELECT COUNT(*) FROM attendance WHERE team_id = ?", (team_id,))
            test = cur.fetchone()[0]
    
            # if row already exists, continue
            if test != 0:
                continue
            else:
                avg2023_str = school_data[schools]["2023_average"]
                avg2023 = int(avg2023_str.replace(",", ""))

                avg2022_str = school_data[schools]["2022_average"]
                avg2022 = int(avg2022_str.replace(",", ""))

                percent_change_str = school_data[schools]["percentage_change"]
                percent_change = float(percent_change_str.replace("%", ""))
            
                cur.execute("INSERT OR IGNORE INTO attendance (team_id, Average2023, Average2022, percent_change) VALUES (?,?,?,?)", (team_id, avg2023, avg2022, percent_change))
                count+= 1
        else:
            break

        # commits the 25 rows to the database
    conn.commit()
    # return count to check how many rows were added
    return count


    

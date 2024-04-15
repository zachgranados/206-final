import sqlite3
import requests
import os


# reads game data api key from extra file
def get_api_key(filename):
    with open(filename, 'r', encoding="utf-8-sig") as file:
            key = file.read()
            return key

# create database for football game data
def setup_db(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn

def create_team_table(cur, conn):
     cur.execute(
        "CREATE TABLE IF NOT EXISTS teams (team_id INTEGER PRIMARY KEY, school TEXT UNIQUE)"
    )
     
     conn.commit()

def input_25_fbs_team_data(cur, conn, year):
 # creating the request to the api
    url = "https://api.collegefootballdata.com/teams/fbs"
    params = {"year": year}
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {get_api_key('api_key.txt')}"
}
    response = requests.get(url, params=params, headers=headers)

# loads data into a json
    if response.status_code == 200:
        data = response.json()
    else:
        print("Request failed with status code:", response.status_code)

# goes through data and adds 25 teams at a time
    count = 0
    for teams in data:
        # checks if loop as looped 25 times
        if count < 25:
            # verify if this team has been added before
            cur.execute("SELECT COUNT(*) FROM teams WHERE school = ?", (teams["school"],))
            row_count = cur.fetchone()[0]
    
        # if row already exists, continue
            if row_count != 0:
                continue
            else:
                name = teams["school"]
                id = int(teams["id"])
                cur.execute("INSERT OR IGNORE INTO teams (team_id, school) VALUES (?,?)", (id,name))
                count+= 1
        else:
            break
    # commits the 25 rows to the database
    conn.commit()
    # return count to check how many rows were added
    return count


        




# testing functions
result = setup_db("cfb.db")
cur = result[0]
conn = result[1]

create_team_table(cur, conn)


      


    

    
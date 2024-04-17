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

def create_media_type(cur, conn):
    # creates the media_types table, that helps stop duplicate strings
    cur.execute(
        "CREATE TABLE IF NOT EXISTS media_type (media_id INTEGER PRIMARY KEY, type TEXT UNIQUE)"
    )

    # list of all possible media types (got from API documentation)
    media_types = ["tv", "radio", "web", "ppv", "mobile"]

    # loops through list and adds to table
    for i in range(0,len(media_types)):
         cur.execute("INSERT OR IGNORE INTO media_type (media_id, type) VALUES (?,?)", (i,media_types[i]))
    conn.commit()

# set up for game data

def create_game_table(cur, conn):
    cur.execute(
        "CREATE TABLE IF NOT EXISTS game_data (game_id INTEGER PRIMARY KEY, home_id INTEGER, away_id INTEGER, home_score INTEGER, away_score INTEGER)"
    )
    conn.commit()

def input_25_games(cur, conn, year):

    # format request to api
    # creating the request to the api
    url = f"https://api.collegefootballdata.com/games?year={year}&seasonType=regular&division=fbs"
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {get_api_key('api_key.txt')}"
}
    response = requests.get(url, headers=headers)

    # loads data into a json
    if response.status_code == 200:
        data = response.json()
    else:
        print("Request failed with status code:", response.status_code)
    

    # sort through 25 at a time
    # goes through data and adds 25 teams at a time
    count = 0
    for games in data:
        # checks if loop as looped 25 times
        if count < 25:
            # verify if this game has been added before
            cur.execute("SELECT COUNT(*) FROM game_data WHERE game_id = ?", (games["id"],))
            row_count = cur.fetchone()[0]
    
        # if row already exists, continue until game id doesn't exist in db
            if row_count != 0:
                continue
            else:
                id = games["id"]
                home_id = int(games["home_id"])
                away_id = int(games["away_id"])

                home_score = int(games["home_points"])
                away_score = int(games["away_points"])
                
                # adds the game data into the database
                cur.execute("INSERT OR IGNORE INTO game_data (game_id, home_id, away_id, home_score, away_score) VALUES (?,?,?,?,?)", (id, home_id, away_id, home_score, away_score))
                count+= 1
        else:
            break
    # commits the 25 rows to the database
    conn.commit()
    # return count to check how many rows were added
    print(count)







# testing functions
result = setup_db("cfb.db")
cur = result[0]
conn = result[1]

create_team_table(cur, conn)
create_media_type(cur, conn)
create_game_table(cur, conn)

input_25_fbs_team_data(cur, conn, 2023)
input_25_games(cur, conn, 2023)

      


    

    
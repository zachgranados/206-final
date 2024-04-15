import sqlite3
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
        "CREATE TABLE IF NOT EXISTS teams (team_id INTEGER PRIMARY KEY, type TEXT UNIQUE)"
    )
     
     conn.commit()

# testing functions
result = setup_db("cfb.db")
cur = result[0]
conn = result[1]

create_team_table(cur, conn)
      


    

    
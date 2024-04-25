import sqlite3
import requests
import os


# ________________________ TABLE SETUP _____________________________
# create database for football game data
def setup_db(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn

# creates team table that turns strings into ids
def create_team_table(cur, conn):
     cur.execute(
        "CREATE TABLE IF NOT EXISTS teams (team_id INTEGER PRIMARY KEY, school TEXT UNIQUE)"
    )
     
     conn.commit()
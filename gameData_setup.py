import sqlite3
import requests
import os

# this file is used to store all the functions that set up tables in the cfb.db that store game / media data


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

# creates media-type table to store different broadcasting types
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

# creates the game_data table
def create_game_table(cur, conn):
    cur.execute(
        "CREATE TABLE IF NOT EXISTS game_data (game_id INTEGER PRIMARY KEY, home_id INTEGER, away_id INTEGER, home_score INTEGER, away_score INTEGER)"
    )
    conn.commit()




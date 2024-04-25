import csv
import requests
import sqlite3

# calculate the home win rate of each team
def home_team_wins(cur, conn):
    
# get a list of all the home team wins
    cur.execute("""
SELECT
    teams.school AS home_school
FROM
    game_data
INNER JOIN
    teams ON game_data.home_id = teams.team_id
WHERE
    game_data.home_score > game_data.away_score;
""")
    
    home_wins = cur.fetchall()

# creates a dict of all the teams and the number of home wins
    home_wins_dict = {}

    for teams in home_wins:
        if teams[0] not in home_wins_dict:
            home_wins_dict[teams[0]] = 1
        else:
            home_wins_dict[teams[0]] += 1

# gets count of home games

    cur.execute("""
SELECT
    teams.team_id AS team_id,
    teams.school AS team_name,
COUNT(game_data.home_id) AS home_game_count
FROM
    teams
LEFT JOIN
    game_data ON teams.team_id = game_data.home_id
GROUP BY
    teams.team_id, teams.school;
                """)
    
    home_count = cur.fetchall()

    total_games = {}
    for team_data in home_count:
        total_games[team_data[1]] = team_data[2]

    
    # do the final calculations home_wins / total home games
    team_win_rate = {}
    for teams in total_games:
        if teams not in home_wins_dict:
            team_win_rate[teams] = 0
        
        else:
            team_win_rate[teams] = home_wins_dict[teams] / total_games[teams]
    
    return team_win_rate





    

    

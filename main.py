import gameData_setup
import game_data
import game_calcs
import game_visualizations

# carries all the function calls to create the database and run calculations

# sets up the database
result = gameData_setup.setup_db("cfb.db")
cur = result[0]
conn = result[1]

# creates all the needed tables
gameData_setup.create_team_table(cur, conn)
gameData_setup.create_game_table(cur, conn)

# inputs 25 teams at a time
game_data.input_25_fbs_team_data(cur, conn, 2023)
# inputs 25 games at a time
game_data.input_25_games(cur, conn, 2023)


# calculates home win rates
results = game_calcs.home_team_wins(cur, conn)

# prints data
game_calcs.write_data(results)

# creates visualization
game_visualizations.create_scatter_plot(results)
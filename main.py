import gameData_setup
import game_data
import game_calcs
import game_visualizations
import attendance_data
import attendance_calcs

# carries all the function calls to create the database and run calculations

# sets up the database
result = gameData_setup.setup_db("cfb.db")
cur = result[0]
conn = result[1]

# creates all the needed tables
gameData_setup.create_team_table(cur, conn)
gameData_setup.create_game_table(cur, conn)
attendance_data.create_attendance_table(cur, conn)

# inputs 25 teams at a time
game_data.input_25_fbs_team_data(cur, conn, 2023)
# inputs 25 games at a time
game_data.input_25_games(cur, conn, 2023)

# creates data for attendance
results = attendance_data.scrape_data()
# inputs 25 teams into attendance data
attendance_data.insert_25_attendance(results, cur, conn)

# calculates home win rates
results = game_calcs.home_team_wins(cur, conn)

# prints data
game_calcs.write_data(results)

# calculates teams that have increased their attendance
data = attendance_calcs.num_of_increases(cur, conn)
attendance_calcs.write_calcs(data)

# creates visualization
#game_visualizations.create_scatter_plot(results)
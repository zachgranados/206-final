import db_setup
import game_data
import game_calcs
import game_visualizations
import attendance_data
import attendance_calcs
import write_calcs
import attendance_visulizations

def main():
    # sets up the database
    result = db_setup.setup_db("cfb.db")
    cur = result[0]
    conn = result[1]

    # creates all the needed tables if needed
    db_setup.create_team_table(cur, conn)
    db_setup.create_game_table(cur, conn)
    db_setup.create_attendance_table(cur, conn)

    # inputs 25 teams at a time
    team_count = game_data.input_25_fbs_team_data(cur, conn, 2023)

    # team table needs to be complete before attendance table (team id is needed)
    if team_count == 25:
        print("Team Data Incomplete, Please Execute This File Again")
        return

    # creates data for attendance
    results = attendance_data.scrape_data()
    # inputs 25 teams into attendance data
    attendance_count = attendance_data.insert_25_attendance(results, cur, conn)

    # inputs 25 games at a time
    game_count = game_data.input_25_games(cur, conn, 2023)

    # prints a statement saying that data is complete or is not complete
    if game_count == 25 or attendance_count == 25:
        print("Attendance Data or Game Data is Not Complete, Please Execute this File Again")
        return
    else:
        print("Database is Complete")
        # calculates home win rates
        game_results = game_calcs.home_team_wins(cur, conn)
        # calculates teams that have increased their attendance
        attendance_results = attendance_calcs.num_of_increases(cur, conn)
    #writes to one file
        write_calcs.write_file(game_results, attendance_results)
    
    #creates visualization
        game_visualizations.create_barGraph(game_results)
        attendance_visulizations.create_barGraph(attendance_results)
    #extra credit viz
        game_visualizations.create_extra_credit(cur, conn)


main()
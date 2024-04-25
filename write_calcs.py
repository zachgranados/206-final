import attendance_calcs
import game_calcs

def write_file(game_data, attendance_data):
    # Open the file in append mode
    with open("calculations.txt", "a") as file:
        # Call both functions with the file object
        attendance_calcs.write_calcs(attendance_data, file)
        file.write("\n")
        game_calcs.write_data(game_data, file)
import attendance_calcs
import game_calcs
 

def write_file(game_data, attendance_data):
    # Open the file in append mode
    with open("calculations.txt", "a+") as file:
        file.seek(0)
        # check if file is empty
        if file.read().strip() == '':
            # Call both functions with the file object
            file.write("Results from Attendance Calculations:\n")
            attendance_calcs.write_calcs(attendance_data, file)
            file.write("\n")
            file.write("Results from Game Data Calculations:\n")
            game_calcs.write_data(game_data, file)
        else:
            return
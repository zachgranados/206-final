import sqlite3

def num_of_increases(cur, conn):
    cur.execute("""
SELECT teams.school AS School, attendance.percent_change AS Percent_Growth
FROM attendance
INNER JOIN
    teams ON attendance.team_id = teams.team_id
WHERE
    attendance.Average2023 > attendance.Average2022
                """)
    
    results = cur.fetchall()
    return results

def write_calcs(data, file):
    count = len(data)

    total = 0
    for teams in data:
        total += int(teams[1])

    average_increase = total / len(data)

    # Write the header
    file.write(f"{count} Teams Increased Their Attendance\n")
    file.write(f"The Average Increase in Attendance is {average_increase}%\n")
    file.write("\n")
  

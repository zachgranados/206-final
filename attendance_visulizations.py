import seaborn as sns
import matplotlib.pyplot as plt

def create_barGraph(attendance_data):
    # Extract team names and growth values from the list of tuples
    teams, growths = zip(*attendance_data)

    # Sort teams and growths based on growth values
    sorted_data = sorted(zip(teams, growths), key=lambda x: x[1], reverse=True)

    # Get top ten teams and growths
    top_teams, top_growths = zip(*sorted_data[:10])
    top_teams = list(top_teams)
    top_growths = list(top_growths)

    # Create a bar plot using Seaborn
    sns.barplot(x=top_growths, y=top_teams, orient='h')
    plt.title('Attendance Growth (Top 10)')
    plt.xlabel('Growth (%)')
    plt.ylabel('Teams')
    # Rotate y-axis labels by 45 degrees for better readability
    plt.yticks(rotation=45, fontsize=8)
    plt.show()

def extra_credit(cur, conn, team_win_rate):

    results = []
    for teams in team_win_rate:
        cur.execute("SELECT team_id FROM teams WHERE school = ?", (teams,))
        team_id = cur.fetchall()[0][0]

        cur.execute("SELECT Average2023 FROM attendance WHERE team_id = ?", (team_id,))
        attendance = cur.fetchall()[0][0]
        
        win_rate = team_win_rate[teams]

        results.append((attendance, win_rate))
    
    attendance, win_rate = zip(*results)
    attendance = list(attendance)
    win_rate = list(win_rate)

    # Create scatter plot using Seaborn with increased jitter
    sns.scatterplot(x=attendance, y=win_rate)
    plt.title('Attendance vs Win Rate')
    plt.xlabel('Attendance')
    plt.ylabel('Win Rate')

    # Show the plot
    plt.show()


    
    


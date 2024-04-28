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


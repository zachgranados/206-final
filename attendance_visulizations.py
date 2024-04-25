import seaborn as sns
import matplotlib.pyplot as plt

def create_barGraph(attendance_data):
    
    # Extract team names and growth values from the list of tuples
    teams, growths = zip(*attendance_data)

    teams = list(teams)
    growths = list(growths)

    # Create a bar plot using Seaborn
    sns.barplot(x=growths, y=teams, orient='h')
    plt.title('Attendance Growth')
    plt.xlabel('Growth(%)')
    plt.ylabel('Teams')
    # Rotate y-axis labels by 45 degrees for better readability
    plt.yticks(rotation=45, fontsize=4)
    plt.show()
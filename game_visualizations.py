import seaborn as sns
import matplotlib.pyplot as plt

def create_scatter_plot(data):
    # Convert dictionary keys and values into lists
    home_teams = list(data.keys())
    win_rates = list(data.values())

    # Create bar plot using Seaborn
    sns.barplot(x=win_rates, y=home_teams, orient='h')
    plt.xlabel('Win Rate')
    plt.ylabel('Home Team')
    plt.title('Home Team Win Rate')
    # Rotate y-axis labels by 45 degrees for better readability
    plt.yticks(fontsize=4)

    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

def create_barGraph(data):
    # Convert dictionary keys and values into lists
    home_teams = list(data.keys())
    win_rates = list(data.values())

    # Create bar plot using Seaborn
    sns.barplot(x=win_rates, y=home_teams)
    plt.xlabel('Win Rate', fontsize=10)  # Set x-axis label with font size 10
    plt.ylabel('Home Team')
    plt.title('Home Team Win Rate')

    # Set x-axis tick labels font size to 5
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=5)

    plt.tight_layout()
    plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

def create_barGraph(data):
  # Convert dictionary keys and values into lists
    home_teams = list(data.keys())
    win_rates = list(data.values())

    # Sort teams and win_rates based on win rates
    sorted_data = sorted(zip(win_rates, home_teams), reverse=True)
    top_win_rates, top_home_teams = zip(*sorted_data[:25])
    top_win_rates = list(top_win_rates)
    top_home_teams = list(top_home_teams)

    # Create bar plot using Seaborn for the top 25 home win rates
    sns.barplot(x=list(top_win_rates), y=list(top_home_teams), color = "blue")
    plt.xlabel('Win Rate', fontsize=10)  # Set x-axis label with font size 10
    plt.ylabel('Home Team')
    plt.title('Top 25 Home Team Win Rates')

    # Set x-axis tick labels font size to 8
    plt.xticks(fontsize=8)

    plt.tight_layout()
    plt.show()


def create_extra_credit(cur, conn):
    cur.execute("SELECT home_score, away_score FROM game_data")
    data = cur.fetchall()

    # Extract home scores and away scores
    home_scores, away_scores = zip(*data)

    # Determine the outcome (home win or away win) for each game
    outcomes = ['Home Wins' if home_score > away_score else 'Away Wins' for home_score, away_score in data]

    # Define colors based on the outcome
    colors = ['blue' if outcome == 'Home Wins' else 'red' for outcome in outcomes]

    # Create scatter plot using Seaborn
    sns.scatterplot(x=home_scores, y=away_scores,hue=outcomes, palette={'Home Wins': 'blue', 'Away Wins': 'red'}, legend='full')
    plt.title('Home Score vs Away Score')
    plt.xlabel('Home Score')
    plt.ylabel('Away Score')

# Show the plot using Matplotlib
    plt.show()


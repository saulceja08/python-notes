import pandas as pd

data_csv = pd.read_csv('/workspaces/python-notes/cod.csv')

# Print the first 10 rows of the DataFrame
print(data_csv.head(10))

# Get and print the descriptive statistics for 'headshots'
headshot_rank = data_csv['headshots'].describe()
print("Headshot Rank Summary:\n", headshot_rank, "\n")

# Get and print the descriptive statistics for 'wins'
wins_rank = data_csv['wins'].describe()
print("Wins Rank Summary:\n", wins_rank, "\n")

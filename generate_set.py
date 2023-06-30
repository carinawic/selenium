import pandas as pd

input_file = 'lichess_db_puzzle.csv'
output_file = 'puzzles_1800-1900.csv'
min_rating = 1800
max_rating = 1900

df = pd.read_csv(input_file)

filtered_df = df[df['Rating'].between(min_rating, max_rating)]
sorted_df = filtered_df.sort_values('Popularity', ascending=False)
output_df = sorted_df[['PuzzleId']]

output_df.to_csv(output_file, index=False, header=False)
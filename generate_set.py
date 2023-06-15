import pandas as pd

input_file = 'lichess_db_puzzle.csv'
output_file = 'puzzles_2000elo.csv'
rating_condition = 1964

df = pd.read_csv(input_file)

filtered_df = df[df['Rating'] == rating_condition]
sorted_df = filtered_df.sort_values('Popularity', ascending=False)
output_df = sorted_df[['PuzzleId']]

output_df.to_csv(output_file, index=False, header=False)
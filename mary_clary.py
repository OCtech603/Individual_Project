#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

"""Task 1"""
# List of years from 2011 to 2020
years = list(range(2011, 2021))

# List of movie durations
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary
movie_dict = {
    "years": years,
    "durations": durations
}

"""Task 2"""
# Create a DataFrame
durations_df = pd.DataFrame(movie_dict)
print(durations_df)

"""Task 3"""
# Create a line plot
plt.plot(durations_df['years'], durations_df['durations'], marker='o')

# Add title and labels
plt.title("Netflix Movie Durations 2011-2020")
plt.xlabel("Year")
plt.ylabel("Duration (minutes)")

"""Task 4"""
# Load the CSV file into a DataFrame
csv_file_path = "datasets/netflix_data.csv"
netflix_df = pd.read_csv(csv_file_path)

# Print the first five rows of the DataFrame
print(netflix_df.head())

"""Task 5"""
# Subset rows where type is "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Subset columns title, country, genre, release_year, and duration
columns_to_keep = ['title', 'country', 'genre', 'release_year', 'duration']
netflix_movies_col_subset = netflix_df_movies_only[columns_to_keep]

# Print the first five rows of netflix_movies_col_subset
print(netflix_movies_col_subset.head())

"""Task 6"""
# Add title and labels
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release Year")
plt.ylabel("Duration (minutes)")

# Show the plot
plt.show()
"""Task 7"""
# Create a new DataFrame containing only short movies (duration < 60)
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]

# Print the first 20 rows of short_movies
print(short_movies.head(20))

"""Task 8"""
# Initialize an empty list to store colors
colors = []

# Use a loop to determine colors based on genre
for genre in netflix_movies_col_subset['genre']:
    if genre == 'Children':
        colors.append('red')
    elif genre == 'Documentaries':
        colors.append('blue')
    elif genre == 'Stand-Up':
        colors.append('green')
    else:
        colors.append('black')

# Print the first 10 values of the colors list
print(colors[:10])

"""Task 9"""
# Create a scatter plot with modified colors
plt.figure(figsize=(10, 6))
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'], c=colors, alpha=0.5)

# Add title and labels
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release Year")
plt.ylabel("Duration (minutes)")

# Show the plot
plt.show()

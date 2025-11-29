import pandas as pd

# Load dataset
df = pd.read_csv('movies.csv')

# Show top rated movies
top_movies = df.sort_values(by='Rating', ascending=False).head(5)
print("Top 5 Movies:\n", top_movies[['Title','Rating']])

# Filter by genre
genre = input("Enter genre to filter movies: ")
genre_movies = df[df['Genre'].str.contains(genre, case=False)]
print(f"\nMovies in {genre} genre:\n", genre_movies[['Title','Rating']])

# Simple recommendation based on rating > 8
recommended = df[df['Rating'] >= 8.0]
print("\nRecommended Movies:\n", recommended[['Title','Rating']])

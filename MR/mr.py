import pandas as pd

# Step 1: Load the movie data
df = pd.read_csv('MR/movies.csv')  # Adjust the path if necessary

# Step 2: Combine the 'Genre', 'Director', and 'Notable Actors' into one text field for each movie
df['combined'] = df['Genre'] + ' ' + df['Director'] + ' ' + df['Notable Actors']

# Step 3: Create a simple similarity function (based on matching words in the combined text)
def calculate_similarity(movie1, movie2):
    # Convert both movie strings to lowercase to avoid case differences
    movie1 = movie1.lower()
    movie2 = movie2.lower()
    
    # Split both movies' text into words
    words1 = set(movie1.split())
    words2 = set(movie2.split())
    
    # Calculate the Jaccard similarity (ratio of common words to total unique words)
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    if len(union) == 0:  # To avoid division by zero
        return 0
    
    return len(intersection) / len(union)

# Step 4: Create a function to recommend movies based on similarity
def recommend_movie(movie_title):
    # Get the movie's combined description
    movie_idx = df[df['Title'] == movie_title].index[0]
    movie_combined = df.loc[movie_idx, 'combined']
    
    # Calculate similarity scores between the chosen movie and all other movies
    similarity_scores = []
    
    for idx, row in df.iterrows():
        if idx != movie_idx:
            similarity_score = calculate_similarity(movie_combined, row['combined'])
            similarity_scores.append((row['Title'], similarity_score))
    
    # Sort the movies by similarity score (highest to lowest)
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top 5 most similar movies
    top_similar_movies = [movie for movie, score in similarity_scores[:5]]
    
    return top_similar_movies

# Step 5: Example usage
movie_title = "Forrest Gump"  # Replace with any movie from your dataset
recommended_movies = recommend_movie(movie_title)

# Display the recommended movies
print(f"Movies similar to {movie_title}:\n")
for movie in recommended_movies:
    print(movie)

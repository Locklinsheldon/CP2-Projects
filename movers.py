# Function to load movies from a file
def load_movies(file_path):
    movies = []
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split(",")
            movie = {
                "title": data[0],
                "genre": data[1],
                "director": data[2],
                "length": int(data[3]),
                "actors": data[4:]
            }
            movies.append(movie)
    return movies

# Function to filter movies based on user input
def filter_movies(filters, movies):
    filtered = movies
    for key, value in filters.items():
        filtered = [movie for movie in filtered if movie[key] == value or value in movie.get(key, [])]
    return filtered

# Main Program
def movie_recommender():
    print("Welcome to the Movie Recommender!")
    movies = load_movies("movies.txt")  # Load movies from the file
    print("Filters available: genre, director, length, actors")
    filters = {}

    while True:
        user_input = input("Enter a filter (e.g., genre:Sci-Fi) or 'done' to search: ")
        if user_input.lower() == "done":
            break
        try:
            key, value = user_input.split(":")
            filters[key.strip()] = value.strip()
        except ValueError:
            print("Invalid input format. Please use 'key:value'.")

    recommendations = filter_movies(filters, movies)
    print("\nRecommendations:")
    for movie in recommendations:
        print(f"{movie['title']} ({movie['genre']}, Directed by {movie['director']})")

    # Option to print the full movie list
    print("\nDo you want to see the full movie list? (yes/no)")
    if input().lower() == "yes":
        print("\nFull Movie List:")
        for movie in movies:
            print(f"{movie['title']} ({movie['genre']}, Directed by {movie['director']})")

# Run the program
movie_recommender()

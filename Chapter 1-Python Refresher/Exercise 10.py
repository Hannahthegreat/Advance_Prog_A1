# Create a dictionary for film details
film_details = {
    "Inception": {
        "Director": "Christopher Nolan",
        "Year": 2010,
        "Genre": "Science Fiction",
        "Rating": 8.8
    },
    "The Shawshank Redemption": {
        "Director": "Frank Darabont",
        "Year": 1994,
        "Genre": "Drama",
        "Rating": 9.3
    },
    "The Godfather": {
        "Director": "Francis Ford Coppola",
        "Year": 1972,
        "Genre": "Crime",
        "Rating": 9.2
    },
    "Pulp Fiction": {
        "Director": "Quentin Tarantino",
        "Year": 1994,
        "Genre": "Crime",
        "Rating": 8.9
    },
    "Forrest Gump": {
        "Director": "Robert Zemeckis",
        "Year": 1994,
        "Genre": "Drama",
        "Rating": 8.8
    }
}

# Display film details using a loop
for title, details in film_details.items():
    print(f"\n{title} Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

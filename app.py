MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'title': title.lower(),
        'director': director.lower(),
        'year': year
    })


def print_movie(movie):
    print(f"{movie['title'].title()} was released in {movie['year']} year and directed by {movie['director'].title()}.")


def list_movies():
    for movie in movies:
        print_movie(movie)


def find_movie():
    search_query = input("Please enter the name/release date/director of the movie: ")
    for movie in movies:
        if search_query.lower() in movie.values():
            print_movie(movie)


user_options = {
    'a': add_movie,
    'l': list_movies,
    'f': find_movie
}


def menu():
    command = input(MENU_PROMPT)
    while command != 'q':
        if command in user_options:
            user_options[command]()
        else:
            print('Unknown command. Please try again.')
        command = input(MENU_PROMPT)


menu()

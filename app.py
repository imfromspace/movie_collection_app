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


def list_movies():
    for movie in movies:
        print(f"> {movie['title'].title()}")


def find_movie(search_query):
    for movie in movies:
        if search_query.lower() in movie.values():
            print(f"{movie['title'].title()} was released in {movie['year']} year and directed by {movie['director'].title()}.")


command = input(MENU_PROMPT)
while command != 'q':
    if command == 'a':
        add_movie()
    if command == 'f':
        find_movie(input("Please enter the name/release date/director of the movie: "))
    if command == 'l':
        list_movies()
    command = input(MENU_PROMPT)

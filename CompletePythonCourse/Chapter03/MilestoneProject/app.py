movies = []

def addMovie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        "title": title,
        "director": director,
        "year": year
    })

def listMovies():
    if not movies:
            print("You have no movies")
    else:
        print("Here are your movies:")
        for movie in movies:
            printMovie(movie)
            
            
def findMovie():
    
    find_by = input("What property of the movie do you want to search by? (title, director, year): ")
    
    if find_by != "title" and find_by != "director" and find_by != "year":
        print("Invalid property")
        return
    
    looking_for = input("What are you looking for? ")
    
    find_by_attribute(looking_for, lambda x: x[find_by])
    

def find_by_attribute(expected, finder):
    found = []
    
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)

    if found:
        print("I found these movies:")
        for movie in found:
            printMovie(movie)
    else:
        print("No movies found")


def printMovie(movie):
    print(f"{movie['title']} ({movie['year']}) directed by {movie['director']}")


user_options = {
    "a": addMovie,
    "l": listMovies,
    "f": findMovie
}

def menu():
    MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, 'q' to quit: "
    
    selection = input(MENU_PROMPT)

    while selection != "q":
        if selection in user_options:
            selected_func = user_options[selection]
            selected_func()
        else:
            print("Invalid selection")
            
        selection = input(MENU_PROMPT)
        
    print("Goodbye!")


menu()
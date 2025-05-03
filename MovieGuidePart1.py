# Carl Louy, CIS261, MovieGuidePart1

def display_menu():
    print("\n==============================")
    print("     Movie List Manager")
    print("==============================")
    print("1. Display movie titles")
    print("2. Add a movie")
    print("3. Delete a movie")
    print("4. Exit")
    print("==============================")

def initialize_movie_list():
    return ["The Shawshank Redemption", "Inception", "The Matrix"]

def display_movies(movie_list):
    if not movie_list:
        print("The movie list is currently empty.")
    else:
        print("\nCurrent Movie List:")
        for idx, movie in enumerate(movie_list, start=1):
            print(f"{idx}. {movie}")

def add_movie(movie_list):
    new_movie = input("Enter the title of the movie to add: ").strip()
    if new_movie:
        movie_list.append(new_movie)
        print(f'"{new_movie}" has been added to the list.')
    else:
        print("No title entered. Nothing added.")

def delete_movie(movie_list):
    display_movies(movie_list)
    try:
        index = int(input("Enter the number of the movie to delete: "))
        if 1 <= index <= len(movie_list):
            removed_movie = movie_list.pop(index - 1)
            print(f'"{removed_movie}" has been removed from the list.')
        else:
            print("Invalid number. No movie deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    movie_list = initialize_movie_list()
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            display_movies(movie_list)
        elif choice == '2':
            add_movie(movie_list)
            display_movies(movie_list)
        elif choice == '3':
            delete_movie(movie_list)
            display_movies(movie_list)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid command. Please choose a valid option.")

if __name__ == "__main__":
    main()
# Use a while loop to add genres to a list until the enter 'END'
# List out each genre, assigning each one an incrementing number starting at 1
# Choose a genre and include a special message when listing it
# Update the application to use a menu and functions for the following:
# Get Genres
# List Genres
# Exit

genres = []


# TODO add a genre get_menu_option function
def get_menu_option():
    print("Genre tracker: ")
    print(f"\t1: Add Genres")
    print(f"\t2: List Genres")
    print(f"\t3: End")
    return int(input(f"\tSelect an option: "))

# TODO add a  add_genre funciton
def add_genres():
    current_genre = input(f"\tEnter a genre: ")
    while current_genre != 'END':
        genres.append(current_genre)
        current_genre = input(f"\tEnter a genre: ")




# TODO add a list_genre fucntion 
def list_genre():
    if len(genres) > 0:
        for genre in genres:
            if genre.lower() == 'country':
                print('choice appended')
            else:
                print(f"/{genre}")
    else:
        print(f"\n\nADD GENRES FIRST\n\n")




while True:
    choice = get_menu_option()
    if choice == 1:
        add_genres()
    elif choice == 2:
        list_genre()
    else:
        break


from utils import database_sqlite as database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all book
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
    database.create_book_db()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == "a":
            prompt_add_book()
        elif user_input == "l":
            list_book()
        elif user_input == "r":
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command.Please try again.")

        user_input = input(USER_CHOICE)
        

def prompt_add_book():
    name = input("Enter the new book name: ")
    author = input("Enter the new book author:")
    database.add_book(name, author)


def list_book():
    books = database.get_all_books()
    if not books:
        print("You have no books saved")
        return
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")
        
def prompt_read_book():
    name = input("Enter the name of the book you just finished reading: ")
    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the name of the book you want to delete: ")
    database.delete_book(name)


menu()
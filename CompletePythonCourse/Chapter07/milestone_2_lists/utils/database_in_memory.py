"""
Store the data in a list.

"""

books = []


def create_book_db():
    pass

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})
    
    
def get_all_books():
    return books
          

def mark_book_as_read(name):
    for book in books:
        if book["name"] == name:
            book['read'] = True
    
    
def delete_book(name):
    global books
    books = [book for book in books if book["name"] != name]

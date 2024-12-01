"""
Store the data in a csv format.
Format of the csv: name,author,read
"""

import os

BOOK_DB_PATH = "./Chapter07/milestone_2_lists/book_db.txt"

def create_book_db():
    if os.path.exists(BOOK_DB_PATH):
        return
    with open(BOOK_DB_PATH, "w") as f:
        pass

def add_book(name, author):
    with open(BOOK_DB_PATH, 'a') as file:
        file.write(f'{name},{author},False\n')
    
    
def get_all_books():
    with open(BOOK_DB_PATH, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
        
        return [
            {'name': line[0], 'author': line[1], 'read': _str_to_bool(line[2])} 
            for line in lines
        ]
    
    # my implementation
    # books = []
    # with open(BOOK_DB_PATH, 'r') as file:
    #     lines = file.readlines()
    
    # lines = [line.strip() for line in lines]
    # for line in lines:
    #     book_data = line.split(",")
    #     books.append({'name': book_data[0], 'author': book_data[1], 'read': str_to_bool(book_data[2])})
        
    # return books
          

def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book['read'] = True
    _save_all_books(books)
    
    
def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book["name"] != name]
    _save_all_books(books)


def _save_all_books(books):
    with open(BOOK_DB_PATH, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")
            
        
def _str_to_bool(s):
    s = s.lower().strip()
    if s == "true":
        return True
    elif s == "false":
        return False
    else:
        raise ValueError(f"Cannot convert '{s}' to a boolean")
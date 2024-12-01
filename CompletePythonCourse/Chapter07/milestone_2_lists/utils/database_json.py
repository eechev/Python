"""
Store the data in json.
[
    {
        'name': 'Clean Code',
        'author': 'Robert',
        'read': True
    }
]

"""

import os
import json

BOOK_DB_PATH = "./Chapter07/milestone_2_lists/book_db.json"

def create_book_db():
    if os.path.exists(BOOK_DB_PATH):
        return
    with open(BOOK_DB_PATH, "w") as file:
        json.dump([], file)

def add_book(name, author):
    books = get_all_books()
    books.append({"name": name, "author": author, "read": False})
    _save_all_books(books)
    
def get_all_books():
    with open(BOOK_DB_PATH, 'r') as file:
        return json.load(file)

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
        json.dump(books, file)
            
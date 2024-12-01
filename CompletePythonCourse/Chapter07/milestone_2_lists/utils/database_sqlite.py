"""
Store the data in an sqlite database.

"""
import os
from .database_connection import DatabaseConnection

BOOK_DB_PATH = "./Chapter07/milestone_2_lists/data.db"

def create_book_db():
    if os.path.exists(BOOK_DB_PATH):
        return
    with DatabaseConnection(BOOK_DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")
        

def add_book(name, author):
    with DatabaseConnection(BOOK_DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM books WHERE name = ? ", (name, ))
        count = cursor.fetchone()[0]
        if count > 0:
            return
        cursor.execute("INSERT INTO books VALUES(?, ? , ?)", (name, author, 0))

    
def get_all_books():
    with DatabaseConnection(BOOK_DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        
    return [
            {'name': book[0], 'author': book[1], 'read': _str_to_bool(book[2])} 
            for book in books
        ]
        

def mark_book_as_read(name):
    with DatabaseConnection(BOOK_DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET read = ? WHERE name = ?",(1, name))

    
    
def delete_book(name):
    with DatabaseConnection(BOOK_DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE name = ?",(name,))
        conn.commit()


def _str_to_bool(s):
    if s == 1:
        return True
    elif s == 0:
        return False
    else:
        raise ValueError(f"Cannot convert '{s}' to a boolean")
import json
import os

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author
        }

def load_books(filename='books.json'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        books_data = json.load(file)
        return [Book(**book) for book in books_data]

def save_books(books, filename='books.json'):
    with open(filename, 'w') as file:
        json.dump([book.to_dict() for book in books], file, indent=4)

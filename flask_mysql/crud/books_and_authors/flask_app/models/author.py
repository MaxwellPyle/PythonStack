from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self,data):
        self.id = data['id']

        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.favorite_books = []
    

    @classmethod
    def get_all(cls):
        authors = []

        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        for author in results:
            authors.append(cls(author))

        return authors

    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        results = connectToMySQL('books_schema').query_db(query,data)
        return results

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)

        author = cls(results[0])

        for row in results:
            data = {
                'id': row['books.id'],
                'title': row['title'],
                'num_of_pages': row['num_of_pages'],
                'created_at': row['books.created_at'],
                'updated_at': row['books.updated_at']
            }
            author.favorite_books.append(book.Book(data))
        return author
    
    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data)

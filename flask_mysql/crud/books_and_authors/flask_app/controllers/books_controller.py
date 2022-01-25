from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/books')
def books():
    return render_template('books.html',all_books = Book.get_all())

@app.route('/books/create',methods=['POST'])
def create_book():
    data = {
        'title':request.form['title'],
        'num_of_pages':request.form['num_of_pages']
    }

    book_id = Book.save(data)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_book(id):
    data = {
        'id':id
    }
    return render_template('show_book.html',book=Book.get_by_id(data),authors=Author.get_all())

@app.route('/books/addfav',methods=['POST'])
def add_favorite():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/books/{request.form['book_id']}")
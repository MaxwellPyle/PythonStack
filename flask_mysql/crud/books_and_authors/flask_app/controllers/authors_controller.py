from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template('authors.html',authors_list = Author.get_all())

@app.route('/authors/create',methods=['POST'])
def create_author():
    data = {
        'name': request.form['name']
    }
    Author_id = Author.save(data)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def show_author(id):
    data = {
        'id': id
    }
    
    return render_template('show_author.html',author=Author.get_by_id(data),books=Book.get_all())

@app.route('/authors/addfav',methods=['POST'])
def add_fav():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/authors/{request.form['author_id']}")

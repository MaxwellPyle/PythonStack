from flask import  render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def init():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('index.html',all_dojos = Dojo.get_all())

@app.route('/dojos/create',methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        'id':id
    }
    return render_template('dojos.html',dojo = Dojo.get_one_dojo(data))
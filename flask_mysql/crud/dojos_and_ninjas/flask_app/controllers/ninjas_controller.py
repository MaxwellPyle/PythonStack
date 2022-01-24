from flask import  render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.dojo import dojo
from flask_app.models.ninja import ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html',dojos = dojo.Dojo.get_all())


@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')
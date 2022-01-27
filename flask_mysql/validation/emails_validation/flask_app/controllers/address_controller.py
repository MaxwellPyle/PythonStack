from flask_app import app
from flask_app.models.address import Address
from flask import redirect, render_template, request

@app.route('/')
def index():
    return redirect("/address")

@app.route('/address')
def address():
    return render_template('address.html')

@app.route('/address/add',methods=['POST'])
def add_address():
    if not Address.validate_address(request.form):
        return redirect('/address')
    Address.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html',addresses=Address.get_all())

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    Address.delete(data)
    return redirect('/success')
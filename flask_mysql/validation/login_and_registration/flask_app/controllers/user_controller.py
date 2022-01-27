from flask_app import app
from flask_app.models.user import User
from flask import redirect, render_template, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/add',methods=['POST'])
def save():
    if not User.validate_user(request.form):
        return redirect('/')

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password']),
    }

    user_id = User.save(data)
    session['user_id'] = user_id

    return redirect('/dashboard')

@app.route('/users/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash('Invalid email',"login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid password',"login")
        return redirect('/')
    
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'id': session['user_id']
    }
    return render_template('dashboard.html',user=User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
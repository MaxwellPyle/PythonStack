
import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "safetydance"

@app.route('/')
def gng():
    if "count" not in session:
        session["count"] = random.randint(1,101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session["guess"] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset/')
def reset():
    session.clear()
    return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)

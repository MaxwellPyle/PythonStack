from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",row=8,col=8,color1='red',color2='black')

@app.route('/<int:r>')
def row(r):
    return render_template("index.html",row=r,col=8,color1='red',color2='black')

@app.route('/<int:r>/<int:y>')
def rowcol(r,y):
    return render_template("index.html",row=r,col=y,color1='red',color2='black')

@app.route('/<int:r>/<int:y>/<string:one>')
def row_col_one(r,y,one):
    return render_template("index.html",row=r,col=y,color1=one,color2='black')

@app.route('/<int:r>/<int:y>/<string:one>/<string:two>')
def row_col_two(r,y,one,two):
    return render_template("index.html",row=r,col=y,color1=one,color2=two)

    
if __name__=="__main__":
    app.run(debug=True)

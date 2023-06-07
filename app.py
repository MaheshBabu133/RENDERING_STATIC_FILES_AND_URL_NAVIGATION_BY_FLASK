from doctest import debug
from flask import Flask,render_template
FAI=Flask(__name__)


@FAI.route('/h111')
def h1():
    return render_template('hi.html')

@FAI.route("/static_files")
def static_files():
    return render_template('static_files.html')

if __name__=="__main__":
    FAI.run(debug=True)
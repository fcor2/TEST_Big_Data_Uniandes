# This is app.py, this is the main file called.
from flask import render_template

from myproject import app


# Views
@app.route("/")
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
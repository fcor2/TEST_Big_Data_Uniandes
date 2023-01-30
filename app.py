# coding=utf-8

# import libraries
from flask import Flask, request, jsonify, render_template

# crea el objeto
app = Flask(__name__)

# importa función para calculo
from calculator import calculator

# define calculator

@app.route('/')

# home is displayed to the user first time
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])

def predict():
    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    result = calculator(a, b, operation)

    return render_template('index.html', prediction_text=str(result))

if __name__ == '__main__':
    app.run(debug=True)

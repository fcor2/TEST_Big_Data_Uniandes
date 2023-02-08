from flask import (
    Blueprint,
    render_template,
    request,

)
# importa función para calculo
from myproject.calculator import calculator


calc_blueprint = Blueprint(name = 'calc',
                           import_name=__name__,
                           url_prefix="")

# define calculator
@calc_blueprint.route("/calculadora")
def index():
    return render_template('index.html')

@calc_blueprint.route('/predict', methods = ['POST'])
def predict():
    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    result = calculator(a, b, operation)

    return render_template('index.html', prediction_text=str(result), title = 'Calculadora básica')
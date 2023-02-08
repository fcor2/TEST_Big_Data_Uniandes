import locale
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

from flask import Flask
from flask_bootstrap import Bootstrap4


# Create app
app = Flask(__name__)
bootstrap = Bootstrap4(app)

###
##Configuration dictionary
###
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'topSecretKey'

########################
### Register blueprints
########################

from myproject.calc.views import calc_blueprint
app.register_blueprint(calc_blueprint)
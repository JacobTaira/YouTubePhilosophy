from flask import Blueprint

auth = Blueprint('auth', __name__)

# Defining a view
# whatever is entered here is prefixed by the app.register in _init__.py
@auth.route('auth/')
def home():
    return "<h1>Auth<h1>"
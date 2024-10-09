from flask import Blueprint, jsonify, render_template
from YouTubeAnalysis import generate_quote

views = Blueprint('views', __name__)

generated_quote = generate_quote()


# Defining a view
@views.route('/')
def home():
    return render_template('home.html', text=generated_quote)

# Route to return the generated string when requested by the button
@views.route('/get-quote')
def get_quote():
    return jsonify({'quote': generated_quote})  # Return the stored string as JSON
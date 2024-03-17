import os
from datetime import datetime
from flask import Flask, render_template, request

# Get the absolute path to the templates folder
templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

# Initialize Flask application with custom template folder
app = Flask(__name__, template_folder=templates_dir, static_folder='images')

messages = []

@app.route('/')
def index():
    return render_template('index.html',messages=messages)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='3000')

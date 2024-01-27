#!/usr/bin/python3
"""
Simple Flask web application
Serves page for:
- "/"
- "/hbnb"
- "/c/<text>"
- "/python/<text>"
- "/number/<n>"
- "/number_template/<n>"
"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """Serves requests to the root"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Serves requests to /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    """accepts input from url"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is(text="is cool"):
    """accepts input from url, input is optional"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Displays 'n' is a number only if 'n' is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_number(n):
    """Displays 'n' is a number only if 'n' is an integer,
       uses html template"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

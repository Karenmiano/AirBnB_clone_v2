#!/usr/bin/python3
"""
Simple Flask web application
Serves page for:
- "/"
- "/hbnb"
"""

from flask import Flask
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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

#!/usr/bin/python3
"""
Simple Flask web application
Serves page for:
- "/"
- "/hbnb"
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """Serves requests to the root"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Serves requests to /hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

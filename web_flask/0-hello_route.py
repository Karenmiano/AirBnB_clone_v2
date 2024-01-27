#!/usr/bin/python3
"""
Simple Flask web application
Serves page for "/"
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb():
    """Serves requests to the root"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

#!/usr/bin/python3
"""
Simple Flask web application
Serves page for "/states_list"
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays state list"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def end_session(exception=None):
    """removes current sqlalchemy session after request"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

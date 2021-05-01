#!/usr/bin/python3
""" Module that start a Flask Webb app"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def index(id=None):
    """display a HTML page"""
    data = storage.all("State")
    return render_template('9-states.html', states=data, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

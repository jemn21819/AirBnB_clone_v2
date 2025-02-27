#!/usr/bin/python3
""" Module that start a Flask Webb app"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ display Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """ display C  followed by the value of the text variable"""
    return "C {}".format(text).replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text='is cool'):
    """display Python , followed by the value of the text variable
    default value of text is 'is cool'"""
    return 'Python {}'.format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def show_num(n):
    """ display n is a number only if n is an integer """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_template(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """application must be listening on"""
    app.run(host='0.0.0.0', port='5000')

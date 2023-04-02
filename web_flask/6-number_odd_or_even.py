#!/usr/bin/python3
""" shebang """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Def hello """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Def hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    """ Def C_is_fun """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def Python_is_cool(text='is cool'):
    """ Def Python_is_cool """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_a_numbe(n):
    """ Def n_is_a_number """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template_is_a_number(n):
    """ def n_template_is_a_number """
    return render_template('5-number.html', num=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def n_template_is_a_odd_or_even(n):
    """ Def n_template_is_odd_or_even """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
""" Routes """

from flask import Flask

"""Create an instance from app.create_app()"""
app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route("/")
def index():
    """
    Route index
    """

    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    Route index
    """

    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    """
    Route index
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/")
@app.route("/python/<text>")
def python_route(text="is cool"):
    """
    Route index
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number_route(n):
    """
    Route index
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')

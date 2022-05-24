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


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')

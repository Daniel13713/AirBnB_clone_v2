#!/usr/bin/python3
""" Routes """

from __init__ import app


app.url_map.strict_slashes = False


@app.route("/")
def index():
    """
    Route index
    """

    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')

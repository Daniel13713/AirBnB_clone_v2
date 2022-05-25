#!/usr/bin/python3
""" Routes """

from flask import Flask, render_template, make_response
from models import storage

"""Create an instance from app.create_app()"""
app = Flask(__name__)

app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """
    -----------------------------------------------------------------
    After each request you must remove the current SQLAlchemy Session
    -----------------------------------------------------------------
    """
    storage.close()


@app.route("/states")
def states():
    """
    -------------------
      Route of states
    -------------------
    """
    from models.state import State

    states = storage.all(State).values()  # all states
    states = sorted(states, key=lambda d: d.name)  # sort states by name
    response = render_template("9-states.html", states=states)

    return response


@app.route("/hbnb_filters")
def filters():
    """
    ---------------------------
      Route of cities by state
    ---------------------------
    """
    from models.state import State
    from models.amenity import Amenity

    states = storage.all(State).values()  # all states
    states = sorted(states, key=lambda d: d.name)  # sort by name
    for state in states:
        state.cities = sorted(state.cities, key=lambda d: d.name)

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda d: d.name)
    response = make_response(
        render_template(
            "10-hbnb_filters.html",
            states=states,
            amenities=amenities))

    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')

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


@app.route("/hbnb")
def hbnb():
    """
    ---------------------------
      Route of cities by state
    ---------------------------
    """
    from models.state import State
    from models.amenity import Amenity
    from models.place import Place
    from models.user import User

    states = storage.all(State).values()  # all states
    states = sorted(states, key=lambda d: d.name)  # sort by name
    for state in states:
        state.cities = sorted(state.cities, key=lambda d: d.name)

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda d: d.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda d: d.name)

    users = storage.all(User)

    response = make_response(
        render_template(
            "100-hbnb.html",
            states=states,
            amenities=amenities,
            places=places,
            users=users
            )
        )

    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')

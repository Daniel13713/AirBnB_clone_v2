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


@app.route("/states/<id>")
def cities_states(id):
    """
    ---------------------------
      Route of cities by state
    ---------------------------
    """
    from models.state import State

    states = storage.all(State).values()  # all states
    states = sorted(states, key=lambda d: d.name)  # sort states by name
    ids = [state.id for state in states]
    if id in ids:
        index = ids.index(id)
        state = states[index]
        state.cities = sorted(state.cities,
                              key=lambda d: d.name)  # sort cities by name
        response = render_template("9-states.html", state=state)
    else:
        response = render_template("9-states.html")

    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')

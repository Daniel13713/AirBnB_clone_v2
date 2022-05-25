#!/usr/bin/python3
""" Routes """

from flask import Flask, render_template
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


@app.route("/states_list")
def states():
    """
    -------------------
      Route of states
    -------------------
    """
    from models.state import State

    states = storage.all(State).values()  # all states
    states = sorted(states, key=lambda d: d.name)  # sort by name
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states")
def cities_states():
    """
    -----------------------------------
      Route of cities fro each state
    -----------------------------------
    """
    from models.state import State

    states = storage.all(State).values()  # all states
    states = sorted(states, key=lambda d: d.name)  # sort by name
    for state in states:
        state.cities = sorted(state.cities, key=lambda d: d.name)

    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')

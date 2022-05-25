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
@app.route("/states/<id>")
def states(id=0):
    """
    -------------------
      Route of states
    -------------------
    """
    from models.state import State

    states = storage.all(State).values()  # all states
    states = sorted(states, key=lambda d: d.name)  # sort states by name
    ids = [state.id for state in states]
    if id == 0:
        response = make_response(
            render_template(
                "9-states.html",
                states=states))
    elif id in ids:
        index = ids.index(id)
        state = states[index]
        state.cities = sorted(state.cities,
                              key=lambda d: d.name)  # sort cities by name
        response = make_response(render_template("9-states.html", state=state))
    else:
        response = make_response(render_template("9-states.html"))

    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')

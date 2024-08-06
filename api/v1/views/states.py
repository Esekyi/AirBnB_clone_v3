#!/usr/bin/python3
"""States objects to JSON"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def states():
    """Retrieve all list of items in State object"""
    states = storage.all(State).values()
    list_all_states = []
    for state in states:
        list_all_states.append(state.to_dict())
    return jsonify(list_all_states)


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state(state_id):
    """Retrieve only one item in State object"""
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def del_state(state_id):
    """Deletes a states with the <state_id>"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200

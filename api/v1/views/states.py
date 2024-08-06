#!/usr/bin/python3
"""States objects to JSON"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request


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


@app_views.route("/states/<state_id>", methods=["DELETE"],
                 strict_slashes=False)
def del_state(state_id):
    """Deletes a states with the <state_id>"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def add_state():
    """Adds a state to db"""
    if not request.is_json:
        abort(404, description="Not a JSON")
    data = request.get_json()
    if "name" not in data:
        abort(404, description="Missing name")

    new_state = State(**data)
    storage.new(new_state)
    new_state.save()

    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"],
                 strict_slashes=False)
def update_state(state_id):
    """UPDATES a state with ID <state_id>"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    if not request.is_json:
        abort(404, description="Not a JSON")
    data = request.get_json()
    if not data.get("name"):
        abort(404)
    else:
        setattr(state, "name", data.get("name"))

    storage.save()
    return jsonify(state.to_dict()), 200

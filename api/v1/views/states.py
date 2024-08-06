#!/usr/bin/python3
"""States objects to JSON"""
from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route("/states", methods=["GET"])
def states():
    """Retrieve all list of items in State object"""
    states = storage.all("State").values()
    list_all_states = []
    for state in states:
        list_all_states.append(state.to_dict())
    return jsonify(list_all_states)

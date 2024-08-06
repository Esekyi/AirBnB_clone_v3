#!/usr/bin/python3
"""Returning the status of the api"""
from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route("/status", methods=['GET'])
def index():
    """Returning status of api"""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats():
    """
    Retrieves the number of each object by type

    Returns:
        A JSON dictionary with the count of each object type.
    """
    obj_count = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(obj_count)

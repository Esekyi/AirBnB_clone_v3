#!/usr/bin/python3
"""States objects to JSON"""
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State
from flask import jsonify, abort, request


@app_views.route("/states/<state_id>/cities",
                 methods=["GET"], strict_slashes=False)
def cities(state_id):
    """Retrieve specified list of cities in State object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    list_all_cities = []

    cities = state.cities
    for city in cities:
        list_all_cities.append(city.to_dict())

    return jsonify(list_all_cities)


@app_views.route("/cities/<city_id>", methods=["GET"], strict_slashes=False)
def get_city(city_id):
    """Retrieve only one item in City object form db"""
    city = storage.get(City, city_id)

    if not city:
        abort(404)

    return jsonify(city.to_dict())


@app_views.route("/cities/<city_id>", methods=["DELETE"],
                 strict_slashes=False)
def del_city(city_id):
    """Deletes a city with the <city_id>"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states/<state_id>/cities",
                 methods=["POST"], strict_slashes=False)
def add_city(state_id):
    """Adds a city object to db"""

    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()

    if "name" not in data:
        abort(400, description="Missing name")

    new_city = City(**data)
    new_city.state_id = state.id
    new_city.save()

    return jsonify(new_city.to_dict()), 201


@app_views.route("/cities/<city_id>", methods=["PUT"],
                 strict_slashes=False)
def update_city(city_id):
    """UPDATES a city with ID <city_id>"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore_data = ['id', 'created_at', 'updated_at', 'state_id']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore_data:
            setattr(city, key, value)

    storage.save()

    return jsonify(city.to_dict()), 200

from flask import Blueprint
from flask import jsonify
from flask import request
from database.db import locations
import json

location_blueprint = Blueprint('location', __name__)


@location_blueprint.route('/location', methods=['GET'])
def get_locations():
    locations_array = []
    for location in locations:
        locations_array.append(locations[location])
    return jsonify(locations_array)


@location_blueprint.route('/location/<location_id>', methods=['GET'])
def get_location(location_id):
    location = locations.get(location_id, {'location': 'location not found'})
    return jsonify({'data': location})


@location_blueprint.route('/location/update', methods=['POST'])
def update_location():
    content = request.get_json()
    if content is None:
        return 'Missing content', 400

    employees[content['id']] = content
    return 'Lugar actualizado'


@location_blueprint.route('/location/delete/<location_id>', methods=['GET'])
def delete_location(location_id):
    locations.pop(location_id)
    return 'Lugar borrado'


@location_blueprint.route('/location/add', methods=['POST'])
def create_location():
    content = request.get_json()
    if content is None:
        return 'Missing content', 400
    print(content)
    location = locations.get(content['id'])

    if location is not None:
        return f'Un lugar con el nombre: {content["name"]} ya existe', 409

    location[content['id']] = content

    return jsonify(locations)
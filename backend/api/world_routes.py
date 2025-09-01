from flask import Blueprint
from flask import jsonify
from flask import request
from database.db import worlds
import json

world_blueprint = Blueprint('world', __name__)


@world_blueprint.route('/world', methods=['GET'])
def get_worlds():
    worlds_array = []
    for world in worlds:
        worlds_array.append(worlds[world])
    return jsonify(worlds_array)


@world_blueprint.route('/world/<world_id>', methods=['GET'])
def get_world(world_id):
    world = worlds.get(world_id, {'world': 'world not found'})
    return jsonify({'data': world})


@world_blueprint.route('/world/update', methods=['POST'])
def update_world():
    content = request.get_json()
    if content is None:
        return 'Missing content', 400

    employees[content['id']] = content
    return 'Mundo actualizado'


@world_blueprint.route('/world/delete/<world_id>', methods=['GET'])
def delete_world(world_id):
    worlds.pop(world_id)
    return 'Mundo borrado'


@world_blueprint.route('/world/add', methods=['POST'])
def create_world():
    content = request.get_json()
    if content is None:
        return 'Missing content', 400
    print(content)
    world = worlds.get(content['id'])

    if world is not None:
        return f'El mundo con el seed: {content["seed"]} ya existe', 409

    world[content['id']] = content

    return jsonify(worlds)
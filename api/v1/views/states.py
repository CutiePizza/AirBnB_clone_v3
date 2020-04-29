#!/usr/bin/python3
"""
States file
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.state import State


@app_views.route('/states/')
def get_all_states():
    """
    get states
    """
    all_states = storage.all(State).values()
    lista = []
    for i in all_states:
        lista.append(i.to_dict())
    return jsonify(lista)


@app_views.route('states/<state_id>', methods=['GET'])
def get_by_id(state_id):
    """
    get state by id
    """
    state = storage.get(State, state_id).to_dict()
    return jsonify(state)


@app_views.route('states/<state_id>', methods=['DELETE'])
def delete_by_id(state_id):
    """
    delete state by id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    else:
        storage.delete(state)
        dic = {}
        return jsonify(dic), 200

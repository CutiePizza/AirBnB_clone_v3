#!/usr/bin/python3
"""
States file
"""
from api.v1.views import app_views
from flask import jsonify
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

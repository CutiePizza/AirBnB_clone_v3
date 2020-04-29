from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status')
def all_states():
    """
    get status
    """
    return jsonify(status="OK")

@app_views.route('/stats')
def counts():
    """
    hahah
    """
    return jsonify(result=lista)

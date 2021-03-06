#!/usr/bin/python3
"""
app file
"""
from flask import Flask, render_template, jsonify, Response
from models import storage
from api.v1.views import app_views
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """
    teardown handling
    """
    storage.close()


@app.errorhandler(404)
def handle_error_404(e):
    """
    hadle error 404 not found
    """
    return jsonify(error="Not found"), 404

if __name__ == "__main__":
    """
    main
    """
    from os import getenv
    host1 = getenv('HBNB_API_HOST')
    port1 = getenv('HBNB_API_PORT')
    if host1 is None:
        host1 = "0.0.0.0"
    if port1 is None:
        port = 5000
    app.run(host=host1, port=port1, threaded=True)

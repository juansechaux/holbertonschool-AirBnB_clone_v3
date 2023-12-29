#!/usr/bin/python3
"""
Contains entrypoint
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def clean_up_all(exc):
    '''Función de limpieza que se ejecutará al
    finalizar el contexto de la aplicación'''
    storage.close()


@app.errorhandler(404)
def not_found_error(e):
    '''Error handler 404'''
    return {'error': 'Not Found'}, 404


if __name__ == "__main__":
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')
    if HBNB_API_HOST is None:
        HBNB_API_HOST = '0.0.0.0.'
    if HBNB_API_PORT is None:
        HBNB_API_PORT = '5000'
    app.run(debug=True, threaded=True, host=HBNB_API_HOST, port=HBNB_API_PORT)

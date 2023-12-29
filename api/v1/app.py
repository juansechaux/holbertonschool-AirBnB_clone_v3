#!/usr/bin/python3
"""
Contains entrypoint
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def clean_up_all(exc):
    '''Función de limpieza que se ejecutará al
    finalizar el contexto de la aplicación'''
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    '''Error handler 404'''
    return jsonify({'error': 'Not Found'}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)

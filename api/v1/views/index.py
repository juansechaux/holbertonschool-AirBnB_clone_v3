#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def test_status():
    '''Test the status of the route'''
    return jsonify({'status': 'OK'})
from flask import jsonify, request
from http import HTTPStatus

from app.models.serie_model import Serie


def create():
    data = request.get_json()
    result_create = Serie.create_serie(data)
    if result_create == 'erro':
        return  {"msg": "Serie already registered"}, 409

    return jsonify(result_create), 201

def series():
    result_get_all = Serie.get_all_series()

    return jsonify({"data":result_get_all }), 200

def select_by_id(serie_id):
    result_search = Serie.filter_serie(serie_id)

    if not result_search:
        return jsonify({"error": "Not Found"}), 404

    return jsonify({"data":result_search}), 200
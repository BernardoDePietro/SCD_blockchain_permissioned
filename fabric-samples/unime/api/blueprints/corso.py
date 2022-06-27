from flask import Blueprint, request
from flask.json import jsonify
from models.corso_model import Corso
from schemas.corso_schema import corso_schema, corso_schemas
from config_db import db

corso_bp = Blueprint('corso_bp', __name__)

@corso_bp.route("/corso", methods=["GET"])
def get_corsi():
    all_corso = Corso.query.all()
    result = corso_schemas.dump(all_corso)
    return jsonify(result)

@corso_bp.route("/corso", methods=["POST"])
def add_corso():
    id_dipartimento = request.json['id_dipartimento']
    nome = request.json['nome']
    new_corso = Corso(nome, id_dipartimento)
    db.session.add(new_corso)
    db.session.commit()
    return corso_schema.jsonify(new_corso)

@corso_bp.route("/corso/<id>", methods=["GET"])
def get_one_corso(id):
    corso = Corso.query.get(id)
    return corso_schema.jsonify(corso)

@corso_bp.route("/corso/<id>", methods=["PUT"])
def update_corso(id):
    corso = Corso.query.get(id)
    corso.nome = request.json['nome']
    db.session.commit()
    return corso_schema.jsonify(corso)

@corso_bp.route("/corso/<id>", methods=["DELETE"])
def delete_corso(id):
    corso = Corso.query.get(id)
    db.session.delete(corso)
    db.session.commit()
    return corso_schema.jsonify(corso)
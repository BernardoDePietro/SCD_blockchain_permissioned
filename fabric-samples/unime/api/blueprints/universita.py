from flask import Blueprint, request, sessions
from flask.json import jsonify
from models.universita_model import Universita
from schemas.universita_schema import UniversitaSchema, universita_schema, universita_schemas
from config_db import db

universita_bp = Blueprint('universita_bp', __name__)

@universita_bp.route("/universita", methods=["GET"])
def get_universita():
    all_universita = Universita.query.all()
    result = universita_schemas.dump(all_universita)
    return jsonify(result)

@universita_bp.route("/universita", methods=["POST"])
def add_universita():
    id_citta = request.json['id_citta']
    nome = request.json['nome']
    via = request.json['via']
    civico = request.json['civico']
    cap = request.json['cap']
    new_universita = Universita(id_citta, nome, via, civico, cap)
    db.session.add(new_universita)
    db.session.commit()
    return universita_schema.jsonify(new_universita)

@universita_bp.route("/universita/<id>", methods=["GET"])
def get_one_universita(id):
    universita = Universita.query.get(id)
    return universita_schema.jsonify(universita)

@universita_bp.route("/universita/<id>", methods=["PUT"])
def update_universita(id):
    universita = Universita.query.get(id)
    universita.id_citta = request.json['id_citta']
    universita.nome = request.json['nome']
    universita.via = request.json['via']
    universita.civico = request.json['civico']
    universita.cap = request.json['cap']
    db.session.commit()
    return universita_schema.jsonify(universita)

@universita_bp.route("/universita/<id>", methods=["DELETE"])
def delete_universita(id):
    universita = Universita.query.get(id)
    db.session.delete(universita)
    db.session.commit()
    return universita_schema.jsonify(universita)
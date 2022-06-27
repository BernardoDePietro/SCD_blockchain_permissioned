from flask import Blueprint, request
from flask.json import jsonify
from models.citta_model import Citta
from schemas.citta_schema import citta_schema, citta_schemas
from config_db import db

citta_bp = Blueprint('citta_bp', __name__)

@citta_bp.route("/citta", methods=["GET"])
def get_citta():
    all_citta = Citta.query.all()
    result = citta_schemas.dump(all_citta)
    return jsonify(result)

@citta_bp.route("/citta", methods=["POST"])
def add_citta():
    id_nazione = request.json['id_nazione']
    nome = request.json['nome']
    new_citta = Citta(id_nazione, nome)
    db.session.add(new_citta)
    db.session.commit()
    return citta_schema.jsonify(new_citta)

@citta_bp.route("/citta/<id>", methods=["GET"])
def get_one_citta(id):
    citta = Citta.query.get(id)
    return citta_schema.jsonify(citta)

@citta_bp.route("/citta/<id>", methods=["PUT"])
def update_citta(id):
    citta = Citta.query.get(id)
    citta.nome = request.json['nome']
    db.session.commit()
    return citta_schema.jsonify(citta)

@citta_bp.route("/citta/<id>", methods=["DELETE"])
def delete_citta(id):
    citta = Citta.query.get(id)
    db.session.delete(citta)
    db.session.commit()
    return citta_schema.jsonify(citta)
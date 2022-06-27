from flask import Blueprint, request
from flask.json import jsonify
from models.nazione_model import Nazione
from schemas.nazione_schema import nazione_schema, nazione_schemas
from config_db import db

nazione_bp = Blueprint('nazione_bp', __name__)

@nazione_bp.route("/nazione", methods=["GET"])
def get_nazione():
    all_nazione = Nazione.query.all()
    result = nazione_schemas.dump(all_nazione)
    return jsonify(result)

@nazione_bp.route("/nazione", methods=["POST"])
def add_nazione():
    nome = request.json['nome']
    new_nazione = Nazione(nome)
    db.session.add(new_nazione)
    db.session.commit()
    return nazione_schema.jsonify(new_nazione)

@nazione_bp.route("/nazione/<id>", methods=["GET"])
def get_one_nazione(id):
    nazione = Nazione.query.get(id)
    return nazione_schema.jsonify(nazione)

@nazione_bp.route("/nazione/<id>", methods=["PUT"])
def update_nazione(id):
    nazione = Nazione.query.get(id)
    nazione.nome = request.json['nome']
    db.session.commit()
    return nazione_schema.jsonify(nazione)

@nazione_bp.route("/nazione/<id>", methods=["DELETE"])
def delete_nazione(id):
    nazione = Nazione.query.get(id)
    db.session.delete(nazione)
    db.session.commit()
    return nazione_schema.jsonify(nazione)
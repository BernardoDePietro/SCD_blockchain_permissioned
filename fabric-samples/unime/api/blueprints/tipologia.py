from typing import NewType
from flask import Blueprint, request
from flask.json import jsonify
from config_db import db
from models.tipologia_models import Tipologia
from schemas.tipologia_schema import tipologia_schema, tipologie_schema

tipologia_bp = Blueprint('tipologia_bp', __name__)

@tipologia_bp.route("/tipologia", methods=["GET"])
def get_tipologie():
    all_tipologie = Tipologia.query.all()
    result = tipologie_schema.dump(all_tipologie)
    return jsonify(result)

@tipologia_bp.route("/tipologia", methods=["POST"])
def add_tipologia():
    nome = request.json['nome']

    new_tipologia = Tipologia(nome)
    db.session.add(new_tipologia)
    db.session.commit()
    return tipologia_schema.jsonify(new_tipologia)

@tipologia_bp.route("/tipologia/<id>", methods=["GET"])
def get_tipologia(id):
    tipologia = Tipologia.query.get(id)
    return tipologia_schema.jsonify(tipologia)

@tipologia_bp.route("/tipologia/<id>", methods=["PUT"])
def update_tipologia(id):
    tipologia = Tipologia.query.get(id)
    tipologia.nome = request.json['nome']
    db.session.commit()
    return tipologia_schema.jsonify(tipologia)

@tipologia_bp.route("/tipologia/<id>", methods=["DELETE"])
def delete_tipologia(id):
    tipologia = Tipologia.query.get(id)
    db.session.delete(tipologia)
    db.session.commit()
    return tipologia_schema.jsonify(tipologia)
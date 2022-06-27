from flask import Blueprint, request
from flask.json import jsonify
from models.dipartimento_model import Dipartimento
from schemas.dipartimento_schema import dipartimento_schema, dipartimento_schemas
from config_db import db

dipartimento_bp = Blueprint('dipartimento_bp', __name__)

@dipartimento_bp.route("/dipartimento", methods=["GET"])
def get_dipartimento():
    all_dipartimento = Dipartimento.query.all()
    result = dipartimento_schemas.dump(all_dipartimento)
    return jsonify(result)

@dipartimento_bp.route("/dipartimento", methods=["POST"])
def add_dipartimento():
    id_universita = request.json['id_universita']
    nome = request.json['nome']
    via = request.json['via']
    civico = request.json['civico']
    cap = request.json['cap']
    new_dipartimento = Dipartimento(id_universita, nome, via, civico, cap)
    db.session.add(new_dipartimento)
    db.session.commit()
    return dipartimento_schema.jsonify(new_dipartimento)

@dipartimento_bp.route("/dipartimento/<id>", methods=["GET"])
def get_one_dipartimento(id):
    dipartimento = Dipartimento.query.get(id)
    return dipartimento_schema.jsonify(dipartimento)

@dipartimento_bp.route("/dipartimento/<id>", methods=["PUT"])
def update_dipartimento(id):
    dipartimento = Dipartimento.query.get(id)
    dipartimento.nome = request.json['nome']
    dipartimento.via = request.json['via']
    dipartimento.civico = request.json['civico']
    dipartimento.cap = request.json['cap']
    db.session.commit()
    return dipartimento_schema.jsonify(dipartimento)

@dipartimento_bp.route("/dipartimento/<id>", methods=["DELETE"])
def delete_dipartimento(id):
    dipartimento = Dipartimento.query.get(id)
    db.session.delete(dipartimento)
    db.session.commit()
    return dipartimento_schema.jsonify(dipartimento)
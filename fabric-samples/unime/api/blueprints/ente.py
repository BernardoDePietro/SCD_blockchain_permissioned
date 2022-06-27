from flask import Blueprint, request
from flask.json import jsonify
from config_db import db
from models.ente_model import Ente
from schemas.ente_schema import ente_schema, enti_schema

ente_bp = Blueprint('ente_bp', __name__)

@ente_bp.route("/ente", methods=["GET"])
def get_enti():
    all_enti = Ente.query.all()
    result = enti_schema.dump(all_enti)
    return jsonify(result)

@ente_bp.route("/ente", methods=["POST"])
def add_ente():
    id_citta = request.json['id_citta']
    nome = request.json['nome']
    email = request.json['email']
    telefono = request.json['telefono']
    via = request.json['via']
    civico = request.json['civico']
    cap = request.json['cap']
    

    new_ente = Ente(id_citta, nome, email, telefono, via, civico, cap)
    db.session.add(new_ente)
    db.session.commit()
    return ente_schema.jsonify(new_ente)

@ente_bp.route("/ente/<id>", methods=["GET"])
def get_ente(id):
    ente = Ente.query.get(id)
    return ente_schema.jsonify(ente)

@ente_bp.route("/ente/<id>", methods=["PUT"])
def update_ente(id):
    ente = Ente.query.get(id)
    ente.id_citta = request.json['id_citta']
    ente.nome = request.json['nome']
    ente.email = request.json['email']
    ente.telefono = request.json['telefono']
    ente.via = request.json['via']
    ente.civico = request.json['civico']
    ente.cap = request.json['cap']
    
    db.session.commit()
    return ente_schema.jsonify(ente)

@ente_bp.route("/ente/<id>", methods=['DELETE'])
def delete_ente(id):
    ente = Ente.query.get(id)
    db.session.delete(ente)
    db.session.commit()
    return ente_schema.jsonify(ente)
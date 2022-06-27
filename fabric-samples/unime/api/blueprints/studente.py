from flask import Blueprint, request
from flask.json import jsonify
from models.studente_model import Studente
from schemas.studente_schema import studente_schema, studenti_schema
from config_db import db

studente_bp = Blueprint('studente_bp', __name__)

@studente_bp.route("/studente", methods=["GET"])
def get_studenti():
    all_studenti = Studente.query.all()
    result = studenti_schema.dump(all_studenti)
    return jsonify(result)

@studente_bp.route("/studente", methods=["POST"])
def add_studente():
    id_corso = request.json['id_corso']
    nome = request.json['nome']
    cognome = request.json['cognome']
    email = request.json['email']
    password = request.json['password']
    matricola = request.json['matricola']

    new_studente = Studente(id_corso, nome, cognome, email, password, matricola)

    db.session.add(new_studente)
    db.session.commit()

    return studente_schema.jsonify(new_studente)

@studente_bp.route("/studente/<id>", methods=["GET"])
def get_studente(id):
    studente = Studente.query.get(id)
    return studente_schema.jsonify(studente)

@studente_bp.route("/studente/<id>", methods=["PUT"])
def update_studente(id):
    studente = Studente.query.get(id)
    studente.nome = request.json['nome']
    studente.cognome = request.json['cognome']
    db.session.commit()
    return studente_schema.jsonify(studente)

@studente_bp.route("/studente/<id>", methods=["DELETE"])
def delete_studente(id):
    studente = Studente.query.get(id)
    db.session.delete(studente)
    db.session.commit()
    return studente_schema.jsonify(studente)
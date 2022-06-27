from flask import Blueprint, request
from flask.json import jsonify
from models.personale_model import Personale
from schemas.personale_schema import personale_schema, personales_schema
from config_db import db

personale_bp = Blueprint('personale_bp', __name__)

@personale_bp.route("/personale", methods=["GET"])
def get_personale():
    all_personale = Personale.query.all()
    result = personales_schema.dump(all_personale)
    return jsonify(result)

@personale_bp.route("/personale", methods=['POST'])
def add_personale():
    id_dipartimento = request.json['id_dipartimento']
    id_categoria = request.json['id_categoria']
    nome = request.json['nome']
    cognome = request.json['cognome']
    email = request.json['email']
    password = request.json['password']

    new_personale = Personale(id_dipartimento, id_categoria, nome, cognome, email, password)

    db.session.add(new_personale)
    db.session.commit()
    return personale_schema.jsonify(new_personale)

@personale_bp.route("/personale/<id>", methods=['GET'])
def get_one_personale(id):
    personale = Personale.query.get(id)
    return personale_schema.jsonify(personale)

@personale_bp.route("/personale/<id>", methods=["PUT"])
def update_personale(id):
    personale = Personale.query.get(id)
    personale.id_categoria = request.json['id_categoria']
    personale.id_dipartimento = request.json['id_dipartimento']
    personale.nome = request.json['nome']
    personale.cognome = request.json['cognome']
    db.session.commit()
    return personale_schema.jsonify(personale)

@personale_bp.route("/personale/<id>", methods=["DELETE"])
def delete_personale(id):
    personale = Personale.query.get(id)
    db.session.delete(personale)
    db.session.commit()
    return personale_schema.jsonify(personale)
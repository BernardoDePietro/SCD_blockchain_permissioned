from flask import Blueprint, request
from flask.json import jsonify
from models.promotore_model import Promotore
from schemas.promotore_schema import promotore_schema, promotore_schemas
from config_db import db
from werkzeug.security import generate_password_hash

promotore_bp = Blueprint('promotore_bp', __name__)

@promotore_bp.route("/promotore", methods=["GET"])
def get_promotori():
    all_promotori = Promotore.query.all()
    result = promotore_schemas.dump(all_promotori)
    return jsonify(result)

@promotore_bp.route("/promotore", methods=["POST"])
def add_promotore():
    id_ente = request.json['id_ente']
    nome = request.json['nome']
    cognome = request.json['cognome']
    email = request.json['email']
    password = request.json['password']

    new_promotore = Promotore(id_ente, nome, cognome, email, password)

    db.session.add(new_promotore)
    db.session.commit()

    return promotore_schema.jsonify(new_promotore)

@promotore_bp.route("/promotore/<id>", methods=["GET"])
def get_promotore(id):
    promotore = Promotore.query.get(id)
    return promotore_schema.jsonify(promotore)

@promotore_bp.route("/promotore/<id>", methods=["PUT"])
def update_promotore(id):
    promotore = Promotore.query.get(id)
    promotore.nome = request.json['nome']
    promotore.cognome = request.json['cognome']
    promotore.email = request.json['email']
    promotore.password = generate_password_hash(request.json['password'], "pbkdf2:sha256")
    db.session.commit()
    return promotore_schema.jsonify(promotore)

@promotore_bp.route("/promotore/<id>", methods=["DELETE"])
def delete_promotore(id):
    promotore = Promotore.query.get(id)
    db.session.delete(promotore)
    db.session.commit()
    return promotore_schema.jsonify(promotore)
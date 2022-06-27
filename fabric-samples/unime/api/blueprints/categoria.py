import re
from flask import Blueprint, request
from flask.json import jsonify
from models.categoria_model import Categoria
from schemas.categoria_schema import categoria_schema, categorie_schema
from config_db import db

categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route("/categoria", methods=["GET"])
def get_categorie():
    all_categorie = Categoria.query.all()
    result = categorie_schema.dump(all_categorie)
    return jsonify(result)

@categoria_bp.route("/categoria", methods=["POST"])
def add_categoria():
    nome = request.json['nome']
    new_categoria = Categoria(nome)
    db.session.add(new_categoria)
    db.session.commit()
    return categoria_schema.jsonify(new_categoria)

@categoria_bp.route("/categoria/<id>", methods=["GET"])
def get_categoria(id):
    categoria = Categoria.query.get(id)
    return categoria_schema.jsonify(categoria)

@categoria_bp.route("/categoria/<id>", methods=["PUT"])
def update_categoria(id):
    categoria = Categoria.query.get(id)
    categoria.nome = request.json['nome']
    db.session.commit()
    return categoria_schema.jsonify(categoria)

@categoria_bp.route("/categoria/<id>", methods=["DELETE"])
def delete_categoria(id):
    categoria = Categoria.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return categoria_schema.jsonify(categoria)
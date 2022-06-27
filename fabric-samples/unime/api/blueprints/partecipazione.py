from flask import Blueprint, request
from flask.json import jsonify
from config_db import db
from models.partecipazione_model import Partecipazione
from schemas.partecipazione_schema import partecipazione_schema, partecipazioni_schema

partecipazione_bp = Blueprint('partecipazione_bp', __name__)

@partecipazione_bp.route("/partecipazione", methods=["GET"])
def get_partecipazioni():
    all_partecipazioni = Partecipazione.query.all()
    result = partecipazioni_schema.dump(all_partecipazioni)
    return jsonify(result)

@partecipazione_bp.route("/partecipazione", methods=["POST"])
def add_partecipazione():
    id_evento = request.json['id_evento']
    id_studente = request.json['id_studente']

    new_partecipazione = Partecipazione(id_evento, id_studente)
    db.session.add(new_partecipazione)
    db.session.commit()
    return partecipazione_schema.jsonify(new_partecipazione)

@partecipazione_bp.route("/partecipazione/<id>", methods=["GET"])
def get_partecipazione(id):
    partecipazione = Partecipazione.query.get(id)
    return partecipazione_schema.jsonify(partecipazione)

@partecipazione_bp.route("/partecipazione/<id>", methods=["DELETE"])
def delete_partecipazione(id):
    partecipazione = Partecipazione.query.get(id)
    db.session.delete(partecipazione)
    db.session.commit()
    return partecipazione_schema.jsonify(partecipazione)
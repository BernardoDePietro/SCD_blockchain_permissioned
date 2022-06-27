from flask import Blueprint, request
from flask.json import jsonify
from config_db import db
from models.evento_model import Dettaglio, Evento
from schemas.evento_schema import evento_schema, eventi_schema, dettaglio_schema, dettagli_schema

evento_bp = Blueprint('evento_bp', __name__)

@evento_bp.route("/evento", methods=["GET"])
def get_eventi():
    all_eventi = Evento.query.all()
    result = eventi_schema.dump(all_eventi)
    return jsonify(result)

@evento_bp.route("/evento", methods=["POST"])
def add_evento():
    id_tipologia = request.json['id_tipologia']
    id_promotore = request.json['id_promotore']
    nome = request.json['nome']
    descrizione = request.json['descrizione']
    durata = request.json['durata']
    data_inizio = request.json['data_inizio']
    data_fine = request.json['data_fine']
    apertura_iscrizioni = request.json['apertura_iscrizioni']
    chiusura_iscrizioni = request.json['chiusura_iscrizioni']

    new_dettaglio = Dettaglio(descrizione, durata, data_inizio, data_fine, apertura_iscrizioni, chiusura_iscrizioni)
    new_evento = Evento(id_tipologia, id_promotore, nome)
    db.session.add(new_dettaglio)
    db.session.add(new_evento)
    db.session.commit()
    return evento_schema.jsonify(new_evento)

@evento_bp.route("/evento/<id>", methods=["GET"])
def get_evento(id):
    evento = Evento.query.get(id)
    return evento_schema.jsonify(evento)

@evento_bp.route("/evento/<id>", methods=["DELETE"])
def update_evento(id):
    evento = Evento.query.get(id)
    dettaglio = Dettaglio.query.get(id)
    db.session.delete(evento)
    db.session.delete(dettaglio)
    db.session.commit()
    return evento_schema.jsonify(evento)

@evento_bp.route("/evento/dettaglio/<id>", methods=['GET'])
def get_dettaglio(id):
    dettaglio = Dettaglio.query.get(id)
    return dettaglio_schema.jsonify(dettaglio)

@evento_bp.route("/evento/dettaglio/<id>", methods=["PUT"])
def update_dettaglio(id):
    dettaglio = Dettaglio.query.get(id)
    dettaglio.descrizione = request.json['descrizione']
    dettaglio.durata = request.json['durata']
    dettaglio.data_inizio = request.json['data_inizio']
    dettaglio.data_fine = request.json['data_fine']
    dettaglio.apertura_iscrizioni = request.json['apertura_iscrizioni']
    dettaglio.chiusura_iscrizioni = request.json['chiusura_iscrizioni']
    db.session.commit()
    return dettaglio_schema.jsonify(dettaglio)
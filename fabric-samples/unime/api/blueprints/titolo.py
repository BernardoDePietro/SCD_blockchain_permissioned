from crypt import methods
import json
from flask import Blueprint, request, session
from flask.json import jsonify
from blockchain import Blockchain
import string
import random
import time

from config_db import db
from config_ipfs import client
from models.titolo_model import Titolo, Informazione
from schemas.titolo_schema import titolo_schema, titoli_schema, informazione_schema

titolo_bp = Blueprint('titolo_bp', __name__)

@titolo_bp.route("/titolo", methods=["GET"])
def get_titoli():
    all_titoli = Titolo.query.all()
    result = titoli_schema.dump(all_titoli)
    return jsonify(result)

@titolo_bp.route("/titolo/test_ipfs", methods=["POST"])
def test_ipfs_insert():
    with open("test.txt", "a", newline="") as file:
        start = time.time()
        ipfs_hash = client.add("test/Schema.png")['Hash']
        temp = "%.2f" % round((time.time()-start) * 1000, 2)
        file.write(temp+"\n")
        return ipfs_hash

@titolo_bp.route("/titolo/test_mysql", methods=["POST"])
def test_mysql_insert():
    with open("test.txt", "a", newline="") as file:
        start = time.time()
        id_evento = request.json['id_evento']
        id_personale = request.json['id_personale']
        id_studente = request.json['id_studente']
        nome = request.json['nome']
        s = 64
        ipfs_hash = ''.join(random.choices(string.ascii_uppercase + string.digits, k = s))

        new_titolo = Titolo(id_evento, id_personale, id_studente, nome, ipfs_hash)
        db.session.add(new_titolo)
        db.session.commit()
        temp = "%.2f" % round((time.time()-start) * 1000, 2)
        file.write(temp+"\n")
        return "200"

@titolo_bp.route("/titolo/test_fabric", methods=["POST"])
def test_fabric_insert():
    with open("test.txt", "a", newline="") as file:
        start = time.time()
        count = request.json['id_fabric']
        id_studente = request.json['id_studente']
        nome = request.json['nome']
        ipfs_hash = "QmSENLMNB2qsRed9CcYEQ15f3VwBZ6AKjtPqnJMByML9yM"
        b = Blockchain(1)
        b.insertTitolo(count, nome, id_studente, ipfs_hash)
        b1 = Blockchain(2)
        b1.insertTitolo(count, nome, id_studente, ipfs_hash)
        temp = "%.2f" % round((time.time()-start) * 1000, 2)
        file.write(temp+"\n")
        return "200"

@titolo_bp.route("/titolo", methods=["POST"])
def add_titolo():
    data = json.loads(request.form.get('data'))
    id_promotore = data['id_promotore']
    id_evento = data['id_evento']
    id_personale = data['id_personale']
    id_studente = data['id_studente']
    nome = data['nome']
    file = request.files.get('titolo')
    ipfs_hash = client.add(file)['Hash']
    descrizione = data['descrizione']
    data_rilascio = data['data_rilascio']

    new_informazione = Informazione(descrizione, data_rilascio)
    new_titolo = Titolo(id_evento, id_personale, id_studente, nome, ipfs_hash)

    db.session.add(new_informazione)
    db.session.add(new_titolo)
    db.session.commit()

    last_titolo = db.session.query(Titolo).order_by(db.desc(Titolo.id_titolo)).first()
    last_id_titolo = last_titolo.getIdTitolo()

    if(id_promotore == 1):
        b = Blockchain(1)
    else:
        b = Blockchain(2)

    if(id_studente is not None):
        return_value = b.insertTitolo(last_id_titolo, nome, id_studente, ipfs_hash)
    else:
        return_value = b.insertTitolo(last_id_titolo, nome, id_personale, ipfs_hash) 
    if(return_value == '500'):
        return {"error": "500"}

    titolo = Titolo.query.get(last_id_titolo)
    titolo.fabric_hash = return_value
    db.session.commit()
    print(return_value)
    return titolo_schema.jsonify(new_titolo)

@titolo_bp.route("/titolo/<id>", methods=["GET"])
def get_titolo(id):
    titolo = Titolo.query.get(id)
    return titolo_schema.jsonify(titolo)

@titolo_bp.route("/titolo/<id>", methods=["DELETE"])
def delete_titolo(id):
    titolo = Titolo.query.get(id)
    info = Informazione.query.get(id)
    db.session.delete(info)
    db.session.delete(titolo)
    db.session.commit()
    return titolo_schema.jsonify(titolo)

@titolo_bp.route("/titolo/informazione/<id>", methods=['GET'])
def get_informazione(id):
    info = Informazione.query.get(id)
    return informazione_schema.jsonify(info)

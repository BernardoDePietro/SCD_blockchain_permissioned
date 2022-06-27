from sqlalchemy import ForeignKey
from config_db import db

class Titolo(db.Model):
    __tablename__ = 'titolo'
    id_titolo = db.Column(db.Integer, primary_key=True)
    id_evento = db.Column(db.Integer, db.ForeignKey('evento.id_evento'), unique=False, nullable=True)
    id_personale = db.Column(db.Integer, db.ForeignKey('personale.id_personale'), unique=False, nullable=True)
    id_studente = db.Column(db.Integer, db.ForeignKey('studente.id_studente'), unique=False, nullable=True)
    nome = db.Column(db.String(100), unique=False, nullable=False)
    ipfs_hash = db.Column(db.String(256), unique=False, nullable=False)
    fabric_hash = db.Column(db.String(256), unique=True, nullable=True)

    evento = db.relationship("Evento")
    personale = db.relationship("Personale")
    studente = db.relationship("Studente")
    
    def __init__(self, id_evento, id_personale, id_studente, nome, ipfs_hash):
        self.id_evento = id_evento
        self.id_personale = id_personale
        self.id_studente = id_studente
        self.nome = nome
        self.ipfs_hash = ipfs_hash

    def getIdTitolo(self):
        return self.id_titolo

class Informazione(db.Model):
    __tablename__ = 'informazione'
    id_informazione = db.Column(db.Integer, primary_key=True)
    descrizione = db.Column(db.Text, unique=False, nullable=True)
    data_rilascio = db.Column(db.Date, unique=False, nullable=False)

    def __init__(self, descrizione, data_rilascio):
        self.descrizione = descrizione
        self.data_rilascio = data_rilascio
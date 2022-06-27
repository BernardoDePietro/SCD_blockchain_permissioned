from enum import unique
from flask import Flask, json
from sqlalchemy.orm import query
from config_db import db

class Evento(db.Model):
    __tablename__ = 'evento'
    id_evento = db.Column(db.Integer, primary_key=True)
    id_tipologia = db.Column(db.Integer, db.ForeignKey('tipologia.id_tipologia'), unique=False, nullable=False) #relazione
    id_promotore = db.Column(db.Integer, db.ForeignKey('promotore.id_promotore'), unique=False, nullable=True) #relazione
    nome = db.Column(db.String(100), unique=False, nullable=False)

    tipologia = db.relationship("Tipologia")
    promotore = db.relationship("Promotore")

    def __init__(self, id_tipologia, id_promotore, nome):
        self.id_tipologia = id_tipologia
        self.id_promotore = id_promotore
        self.nome = nome

class Dettaglio(db.Model):
    __tablename__ = 'dettaglio'
    id_dettaglio = db.Column(db.Integer, primary_key=True)
    descrizione = db.Column(db.Text, unique=False, nullable=True)
    durata = db.Column(db.Integer, unique=False, nullable=False)
    data_inizio = db.Column(db.Date, unique=False, nullable=False)
    data_fine = db.Column(db.Date, unique=False, nullable=False)
    apertura_iscrizioni = db.Column(db.Date, unique=False, nullable=False)
    chiusura_iscrizioni = db.Column(db.Date, unique=False, nullable=False)

    def __init__(self, descrizione, durata, data_inizio, data_fine, apertura_iscrizioni, chiusura_iscrizioni):
        self.descrizione = descrizione
        self.durata = durata
        self.data_inizio = data_inizio
        self.data_fine = data_fine
        self.apertura_iscrizioni = apertura_iscrizioni
        self.chiusura_iscrizioni = chiusura_iscrizioni
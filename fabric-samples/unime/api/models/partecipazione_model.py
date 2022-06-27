from flask import Flask, json
from sqlalchemy.orm import query
from config_db import db
import datetime

class Partecipazione(db.Model):
    __tablename__ = 'partecipazione'
    id_partecipazione = db.Column(db.Integer, primary_key=True)
    id_evento = db.Column(db.Integer, db.ForeignKey('evento.id_evento'), unique=False, nullable=False)
    id_studente = db.Column(db.Integer, db.ForeignKey('studente.id_studente'), unique=False, nullable=False)
    data_iscrizione = db.Column(db.DateTime, default=datetime.date.today)

    evento = db.relationship("Evento")
    studente = db.relationship("Studente")

    def __init__(self, id_evento, id_studente):
        self.id_evento = id_evento
        self.id_studente = id_studente
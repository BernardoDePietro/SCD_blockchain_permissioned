from flask import Flask, json
from config_db import db

class Nazione(db.Model):
    __tablename__ = 'nazione'
    id_nazione = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, nome):
        self.nome = nome
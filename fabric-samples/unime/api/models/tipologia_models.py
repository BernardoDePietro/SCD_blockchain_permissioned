from flask import Flask, json
from sqlalchemy.orm import query
from config_db import db

class Tipologia(db.Model):
    __tablename__ = 'tipologia'
    id_tipologia = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, nome):
        self.nome = nome
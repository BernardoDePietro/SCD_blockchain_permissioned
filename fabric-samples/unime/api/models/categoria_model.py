from flask import Flask, json
from sqlalchemy.orm import query
from config_db import db

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id_categoria = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, nome):
        self.nome = nome
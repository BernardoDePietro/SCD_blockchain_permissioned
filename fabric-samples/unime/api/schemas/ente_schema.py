from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class EnteSchema(ma.Schema):
    class Meta:
        fields = (
            'id_ente',
            'id_citta',
            'nome',
            'email',
            'telefono',
            'via',
            'civico',
            'cap'
        )

ente_schema = EnteSchema()
enti_schema = EnteSchema(many=True)
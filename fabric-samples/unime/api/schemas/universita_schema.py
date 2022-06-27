from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class UniversitaSchema(ma.Schema):
    class Meta:
        fields = (
            'id_universita',
            'id_citta',
            'nome',
            'via',
            'civico',
            'cap'
        )

universita_schema = UniversitaSchema()
universita_schemas = UniversitaSchema(many=True)
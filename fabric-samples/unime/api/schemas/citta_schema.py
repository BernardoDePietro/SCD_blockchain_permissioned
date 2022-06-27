from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class CittaSchema(ma.Schema):
    class Meta:
        fields = (
            'id_citta',
            'id_nazione',
            'nome'
        )

citta_schema = CittaSchema()
citta_schemas = CittaSchema(many=True)
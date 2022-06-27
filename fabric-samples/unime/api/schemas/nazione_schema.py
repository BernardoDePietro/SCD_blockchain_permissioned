from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class NazioneSchema(ma.Schema):
    class Meta:
        fields = (
            'id_nazione',
            'nome'
        )

nazione_schema = NazioneSchema()
nazione_schemas = NazioneSchema(many=True)
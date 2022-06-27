from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class TipologiaSchema(ma.Schema):
    class Meta:
        fields = (
            'id_tipologia',
            'nome'
        )

tipologia_schema = TipologiaSchema()
tipologie_schema = TipologiaSchema(many=True)
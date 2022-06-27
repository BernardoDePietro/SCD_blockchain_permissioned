from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class PromotoreSchema(ma.Schema):
    class Meta:
        fields = (
            'id_promotore',
            'id_ente',
            'nome',
            'cognome',
            'email',
            'password'
        )

promotore_schema = PromotoreSchema()
promotore_schemas = PromotoreSchema(many=True)
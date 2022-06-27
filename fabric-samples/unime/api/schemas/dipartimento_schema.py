from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class DipartimentoSchema(ma.Schema):
    class Meta:
        fields = (
            'id_dipartimento',
            'id_universita',
            'nome',
            'via',
            'civico',
            'cap'
        )

dipartimento_schema = DipartimentoSchema()
dipartimento_schemas = DipartimentoSchema(many=True)
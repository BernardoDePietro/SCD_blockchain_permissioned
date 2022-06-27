from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class CorsoSchema(ma.Schema):
    class Meta:
        fields = (
            'id_corso',
            'id_dipartimento',
            'nome'
        )

corso_schema = CorsoSchema()
corso_schemas = CorsoSchema(many=True)
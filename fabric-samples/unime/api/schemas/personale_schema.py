from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class PersonaleSchema(ma.Schema):
    class Meta:
        fields = (
            'id_personale',
            'id_dipartimento',
            'id_categoria',
            'nome',
            'cognome',
            'email',
            'password'
        )

personale_schema = PersonaleSchema()
personales_schema = PersonaleSchema(many=True)
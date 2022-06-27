from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class StudenteSchema(ma.Schema):
    class Meta:
        fields = (
            'id_studente',
            'id_corso',
            'nome',
            'cognome',
            'email',
            'password',
            'matricola'
        )

studente_schema = StudenteSchema()
studenti_schema = StudenteSchema(many=True)
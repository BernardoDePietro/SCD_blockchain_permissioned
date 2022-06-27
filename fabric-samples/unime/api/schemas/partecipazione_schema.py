from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class PartecipazioneSchema(ma.Schema):
    class Meta:
        fields = (
            'id_partecipazione',
            'id_evento',
            'id_studente',
            'data_iscrizione'
        )

partecipazione_schema = PartecipazioneSchema()
partecipazioni_schema = PartecipazioneSchema(many=True)
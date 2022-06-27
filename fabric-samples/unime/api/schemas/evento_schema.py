from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class EventoSchema(ma.Schema):
    class Meta:
        fields = (
            'id_evento',
            'id_tipologia',
            'id_promotore',
            'nome'
        )

evento_schema = EventoSchema()
eventi_schema = EventoSchema(many=True)

class DettaglioSchema(ma.Schema):
    class Meta:
        fields = (
            'id_dettaglio',
            'descrizione',
            'durata',
            'data_inizio',
            'data_fine',
            'apertura_iscrizioni',
            'chiusura_iscrizioni'
        )

dettaglio_schema = DettaglioSchema()
dettagli_schema = DettaglioSchema(many=True)
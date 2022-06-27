from config_app import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class TitoloSchema(ma.Schema):
    class Meta:
        fields = (
            'id_titolo',
            'id_evento',
            'id_personale',
            'id_studente',
            'nome',
            'ipfs_hash',
        )

titolo_schema = TitoloSchema()
titoli_schema = TitoloSchema(many=True)

class InformazioneSchema(ma.Schema):
    class Meta:
        fields = (
            'id_informazione',
            'descrizione',
            'data_rilascio'
        )

informazione_schema = InformazioneSchema()
informazioni_schema = InformazioneSchema(many=True)
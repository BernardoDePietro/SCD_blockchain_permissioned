from config_app import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('id_categoria', 'nome')

categoria_schema = CategoriaSchema()
categorie_schema = CategoriaSchema(many=True)
from api import ma
from api.models import Animal, Protetor

class AnimalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Animal
        include_fk = True

    id = ma.auto_field()
    nome = ma.auto_field()
    classe = ma.auto_field()
    ordem = ma.auto_field()
    especie = ma.auto_field()
    protetor_id = ma.auto_field()

class ProtetorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Protetor 

    id = ma.auto_field()
    nome = ma.auto_field()
    animais = ma.Nested(AnimalSchema, many=True)
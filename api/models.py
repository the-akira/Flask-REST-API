from api import db

class Protetor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))

    def __init__(self, nome):
    	self.nome = nome 

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    classe = db.Column(db.String(255))
    ordem = db.Column(db.String(255))
    especie = db.Column(db.String(255))
    protetor_id = db.Column(db.Integer, db.ForeignKey("protetor.id"))
    protetor = db.relationship("Protetor", backref="animais")

    def __init__(self, nome, classe, ordem, especie, protetor_id):
    	self.nome = nome 
    	self.classe = classe 
    	self.ordem = ordem
    	self.especie = especie
    	self.protetor_id = protetor_id
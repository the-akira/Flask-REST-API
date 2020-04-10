from flask import Blueprint, request, jsonify
from api.models import Animal, Protetor
from api.schemas import AnimalSchema, ProtetorSchema
from api import db

main = Blueprint('main', __name__)

protetor_schema = ProtetorSchema()
protetores_schema = ProtetorSchema(many=True)
animal_schema = AnimalSchema()
animais_schema = AnimalSchema(many=True)

@main.route('/', methods=['GET'])
def welcome():
	return jsonify(
		{
			'sobre':'Seja bem-vindo à API de Animais',
			'versão':'0.0.5'
		}
	)

@main.route('/protetor', methods=['POST'])
def post_protetor():
	try:
		nome = request.json['nome']
		protetor = Protetor(nome)
		db.session.add(protetor)
		db.session.commit()
	except KeyError:
		return jsonify({'error':'submit error, check the key'})
	return protetor_schema.jsonify(protetor)

@main.route('/protetores', methods=['GET'])
def get_protetores():
	protetores = Protetor.query.all()
	resultado = protetores_schema.dump(protetores)
	return jsonify(resultado)

@main.route('/protetor/<int:id>', methods=['GET'])
def get_protetor(id):
	protetor = Protetor.query.get(id)
	if protetor:
		return protetor_schema.jsonify(protetor)
	else:
		return jsonify({'error':'protector not found'})

@main.route('/protetor/<int:id>', methods=['PUT'])
def update_protetor(id):
	protetor = Protetor.query.get(id)
	if protetor:
		try:
			nome = request.json['nome']
			protetor.nome = nome
			db.session.commit()
		except KeyError:
			return jsonify({'error':'submit error, check the key'})
	else:
		return jsonify({'error':'no protectors found'})
	return protetor_schema.jsonify(protetor)

@main.route('/protetor/<int:id>', methods=['DELETE'])
def delete_protetor(id):
	protetor = Protetor.query.get(id)
	if protetor: 
		db.session.delete(protetor)
		db.session.commit()
	else:
		return jsonify({'error':'no protectors found'})
	return protetor_schema.jsonify(protetor)

@main.route('/animal', methods=['POST'])
def post_animal():
	try:
		nome = request.json['nome']
		classe = request.json['classe']
		ordem = request.json['ordem']
		especie = request.json['especie']
		protetor_id = request.json['protetor_id']
		animal = Animal(nome, classe, ordem, especie, protetor_id)
		db.session.add(animal)
		db.session.commit()
	except KeyError:
		return jsonify({'error':'submit error, check the keys'})
	return animal_schema.jsonify(animal)

@main.route('/animais', methods=['GET'])
def get_animais():
	animais = Animal.query.all()
	resultado = animais_schema.dump(animais)
	return jsonify(resultado)

@main.route('/animal/<int:id>', methods=['GET'])
def get_animal(id):
	animal = Animal.query.get(id)
	if animal:
		return animal_schema.jsonify(animal)
	else:
		return jsonify({'error':'animal not found'})

@main.route('/animal/<int:id>', methods=['PUT'])
def update_animal(id):
	animal = Animal.query.get(id)
	if animal:
		try:
			nome = request.json['nome']
			classe = request.json['classe']
			ordem = request.json['ordem']
			especie = request.json['especie']
			protetor_id = request.json['protetor_id']
			animal.nome = nome
			animal.classe = classe 
			animal.ordem = ordem 
			animal.especie = especie 
			animal.protetor_id = protetor_id
			db.session.commit()
		except KeyError:
			return jsonify({'error':'submit error, check the keys'})
	else: 
		return jsonify({'error':'no animals found'})
	return animal_schema.jsonify(animal)

@main.route('/animal/<int:id>', methods=['DELETE'])
def delete_animal(id):
	animal = Animal.query.get(id)
	if animal:
		db.session.delete(animal)
		db.session.commit()
	else:
		return jsonify({'error':'no animal found'})
	return animal_schema.jsonify(animal)
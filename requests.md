# Requests

## GET

curl -X GET http://localhost:5000/

curl -X GET http://localhost:5000/protetores

curl -X GET http://localhost:5000/animais

curl -X GET http://localhost:5000/protetor/3

curl -X GET http://localhost:5000/animal/1

## POST

curl -d '{"nome":"Tigre", "classe":"mamifero", "ordem":"carnivoro", "especie": "P. tigris", "protetor_id": 1}' -H "Content-Type: application/json" -X POST http://localhost:5000/animal

curl -d '{"nome":"Lobo-cinzento", "classe":"mamifero", "ordem":"carnivoro", "especie": "C. lupus", "protetor_id": 2}' -H "Content-Type: application/json" -X POST http://localhost:5000/animal

curl -d '{"nome":"Urso-Polar", "classe":"mamifero", "ordem":"carnivoro", "especie": "U. maritimus", "protetor_id": 5}' -H "Content-Type: application/json" -X POST http://localhost:5000/animal

curl -d '{"nome":"Corvo-Comum", "classe":"aves", "ordem":"Passeriformes", "especie": "C. corax", "protetor_id": 3}' -H "Content-Type: application/json" -X POST http://localhost:5000/animal

curl -d '{"nome":"Burrowing Owl", "classe":"aves", "ordem":"Strigiformes", "especie": "A. cunicularia", "protetor_id": 3}' -H "Content-Type: application/json" -X POST http://localhost:5000/animal

curl -d '{"nome":"Eduardo"}' -H "Content-Type: application/json" -X POST http://localhost:5000/protetor

## UPDATE

curl -X PUT -H "Content-Type: application/json" -d '{"nome":"Mateus"}' http://localhost:5000/protetor/1

curl -X PUT -H "Content-Type: application/json" -d '{"nome":"Leoa", "classe":"mamifero", "ordem":"carnivoro", "especie": "felino", "protetor_id": 3}' http://localhost:5000/animal/4

## DELETE

curl -X "DELETE" http://127.0.0.1:5000/protetor/1

curl -X "DELETE" http://127.0.0.1:5000/animal/1
# TD n°3 : Simple API et bonnes pratiques


## Présentation de Flask

[Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application) est un framework python qui permet la rédaction d'API REST.

### Point fort de Flask :

* Framework léger python
* Serveur et Debugger
* Possibilité de test unitaire
* Possibilité de rendre du HTML
* Intègre Google App Engine
* Client-side sessions

### Exemple 
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)

```python 
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercice - Simple API 

Définir une **API** de type REST HTTP/S python à l’aide de Flask.

**CRUD** sur un dictionnaire clé/valeur (**GET**, **POST**, **DELETE**, **PUT**) :
 
* Un endpoint pour afficher la liste
* Un endpoint pour ajouter un élément dans la liste
* Un endpoint pour supprimer un élément dans la liste
* Un endpoint pour modifier un élément via ID.

## Documentation Swagger

**Swagger** est un ensemble d'outils permettant de développer et documenter des API REST.

**Swagger Editor** est un outil en ligne pour déclarer via un manifeste yaml des API au format OpenAPI Specification (OAS).

### Exercice
Ecrire un Swagger pour décrire l’API 

[Swagger Editor](https://editor.swagger.io/)

## Documentation

[REST API selon RedHat](https://www.redhat.com/en/topics/api/what-is-a-rest-api)

[Swagger Editor](https://editor.swagger.io/)

[Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application)

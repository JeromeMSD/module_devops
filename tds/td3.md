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

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World !"

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercice - Installer & Lancer Flask

1. Vérifiez que python3 est installé
```bash 
python3
```

2. Installer Flask 
```bash 
pip install Flask
```

3. Vérifiez que Flask est installé
```bash 
pip freeze
```

4. Créez un fichier `àpp.py`avec en contenu le code de l'exemple de la section précédente
5. Configurez Flask pour ouvrir ce fichier par défault et lancer Flask :
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run 
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

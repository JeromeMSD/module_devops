# TD n°4 - Test Driven Development

Mettre en place le développement piloté par les tests.

## Échauffement

Nous allons commencer par un developpement d'une fonction python en deux itérations.

### 0. Prérequis

Si il n'est pas déjà installé, installer `python3` dans votre environment Linux (`VM` ou `WSL`):

```shell
apt-get install python3
```

La commande `python3 --version && pip3 --version` devrait retourner quelque chose comme ceci:

```shell
Python 3.11.6
pip 23.2.1 from ... (python 3.11)
```

Ensuite, installer la bibliothèque `pytest`:

```shell
pip3 install pytest
```

Créer les fichiers `main.py` et `test.py` qui contiendront respectivement les fonctions à développer et leurs tests.

> [!tip]
> Si cette partie pose des difficultés, demander de l'aide. 🙋‍♀️🙋‍♂️

### 1. Ecrire un test

Commençons par quelque chose de simple et basique, une fonction qui renvoie `Hello World !`. Le test correspondant se représenterait comme suit:

```python
import main

def test_hello():
    assert main.hello() == "Hello World !"
```

Le test défini ci-dessus est **valide** si l'assertion suivante est vraie: 
> **Le retour de la fonction `hello()` de `main` est une chaine de caractères contenant `Hello World !`.**

Ajouter le code ci-dessus dans le fichier `test.py` et exécuter ce test avec la commande `pytest`.

```shell
pytest test.py
```

Vous avez maintenant l'objectif que vous voulez atteindre avec la fonction. 🚀

### 2. Coder

Coder la fonction pour rendre l'assertion vraie. Ajouter dans le fichier `main.py` la fonction `python` suivante :

```python
def hello():
    return "Hello world !"
```

La fonction doit maintenant remplir l'objectif précédemment fixé.

### 3. Tester

Tester la fonction `hello()`.

```shell
pytest test.py
```

> [!tip]
> **Le test passe au vert** - Vous pouvez passer à la suite.

> [!caution]
> **Le test reste au rouge** - Reprenez à l'**étape 2**.

### 4. Refactoriser

À partir d'ici, la fonction répond à l'objectif fixé à l'étape 1.

L'étape de **refactorisation** va permettre d'assurer qualité et respect des bonnes pratiques dans le code livré, refactoriser la fonction `hello()` dans le fichier `main.py`.

> [!note]
> N'oubliez pas: **Refactoriser** c'est améliorer, simplifier et optimiser le code d'une fonction pour le rendre plus pertinent. Par exemple, en rendant une fonction plus modulaire.

```python
def hello(msg="Hello world!"):
    return msg
```

### 5. Confirmer

Exécuter à nouveau les tests pour confirmer que la refactorisation n'a pas d'impact.

```shell
pytest test.py
```

> [!tip]
> **Le test reste est vert** - Félicitation, la fonctionnalité est complète grâce à votre implémentation de la méthode **Red-Green-Refactor** 🚀

> [!caution]
> **Le test passe au rouge** - Une erreur c'est inserée dans le code, recommencer l'itération **4. Refactoriser**.

---

## Mise à l'échelle

Nous allons maintenant mettre à l'échelle la méthodologie.

### Integration continue

Créer une [GitHub Action](./td2.md) qui permet, pour chaque push, d'exécuter les tests via `pytest`.

### Le calendrier

Réaliser une suite de fonction pour créer et gérer des évènements.

Définissons un évènement comme étant un tuple (`T1`, `t`, `n`), où `t` est égal au temps de l’évènement en seconde à partir du timestamp `T1` (date et heure du début de l’évènement). `n` sera le nom de l’évènement.

0. Les évènements sont stockés dans un tableau.
1. Créer un évènement.
2. Retourner une liste d'évènements.
3. Retourner une liste de tous les événements dans l’ordre chronologique.
4. Retourner le nom du premier évènement dans la liste.
5. Retourner le nom du prochain évènement.

> [!important]
> Chacunes des fonctionnalités doivent être représentées par **au moins trois commits**:
> * Un premier commit dont le message suivra le format `test: nom_de_la_fonction()`, contenant le test de la fonction à développer.
> * Un second commit dont le message suivra le format `code: nom_de_la_fonction()`, contenant le code de la fonction à développer.
> * Un troisième commit dont le message suivra le format `refactor: nom_de_la_fonction()`, contenant le code de la fonction à développer.

> [!tip]
> Pour les phases de **code** et de **refactorisation**, vous pouvez tester localement avec `pytest`, et pousser uniquement lors du premier passage au vert et au terme de la refactorisation.

### Bonus - APIfication (facultatif)

Utiliser `Flask` pour transformer cet ensemble de fonctions en une **API REST**.

Exemple d'API Flask à un endpoint:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Placer chacunes de vos fonctions sous une route différente. (ex: `@app.route("/list")`).

```shell
python main.py
```

> [!note]
> [Documentation Flask](https://flask.palletsprojects.com/en/3.0.x/)

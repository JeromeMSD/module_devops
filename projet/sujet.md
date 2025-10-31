[![uB](https://upload.wikimedia.org/wikipedia/fr/c/cc/Logo_EPE_Universit%C3%A9_Bourgogne_Europe.svg)](https://u-bourgogne.fr/) | Polytech Dijon - 4A - ILIA - DevOps <br/><br/> **[ EXAMEN PRATIQUE ]** | [![ESIREM](https://polytech.ube.fr/wp-content/uploads/2023/02/Logo_Reseau_Polytech.svg_-300x191.png)](https://esirem.u-bourgogne.fr/)
:--- |:------------------------------------------------------------------:| ---:
||                  ||

# Sujet projet - Année 2025

> [!warning]
> Avant de commencer, veiller à prendre connaissance des attentes projet [./README.md#exigences-du-projet](./README.md#exigences-du-projet).

Ce projet est à rendre au plus tard le `Vendred 14 novembre 2025 à 23h59`. À partir de cette date, aucun changement (commit, issue ou pull_request) ne sera pris en compte pour la notation.

![PolyStatus](https://github.com/user-attachments/assets/ad8a7ec4-eb29-4ac4-ab15-2f6513b8f4f1)

<br/>

Au cours de ce projet, nous allons réaliser les différentes composantes microservices de suivi d'incident, comme le fait par exemple [DownDetector](https://downdetector.fr/).

## PolyStatus 🚀

Concevoir une grappe de microservice composée d'API simples `Python/Flask` et d'un frontend. Cet ensemble permettra de répondre aux fonctionnalités suivantes :

* ToBeDefined 

Via la déclaration de route `GET` et `POST` vous définirez les fonctions pour répondre aux fonctionnalités si dessus ☝️

**Polytex** sera composé d'au moins 4 microservice. 

- Gestion/suivi des incidents.
- Gestion des profils utilisateurs (CRUD) et identité.
- Gestion des communications (status, banière, emails).
- Recupération de status des autres CSP.
- Serveur de feature flags.
- Frontend.

> [!note]
> Chacun des microservices et le frontend feront l'objet d'un dossier dans le dépôt. (cf. [./README.md#exigences-du-projet](./README.md#exigences-du-projet))

---

### Gestion des objets (API REST et JSON)

L'envoie et le retour de données dans les requêtes et les reponses `HTTP` peut être simplifié via l'utilisation de structure [`JSON`](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation). Vous pourrez gérer vos traitements et/ou transformation de donnée ou de message dans les routes de votre API.

> [!tip]
> Avant de mettre en place les bases Redis, vous pouvez utiliser des dictionnaires en variables locales dans le microservice pour tester vos routes et vos fonctionnalités.

Testez vos routes avec la commande `curl`.

> [!note]
> Gardez en tête l'objectif d'autonomie des microservices, l'idée est de créer des [API REST ](https://www.redhat.com/fr/topics/api/what-is-a-rest-api).

### Stockage

Pour externaliser le stockage des données et garantir leurs conservations en cas redémarrage des microservices, le tout dans une base rapide et sans contrainte, vous pouvez utiliser `redis`.

> [!important]
> Vous êtes libre de choisir le découpage pour le stockage, échanger autour des possibilités et documenter les via issues et fichier Markdown.

#### Qu'est ce que Redis ?

`Redis` est une base de donnée clé/valeur qui vous permettra de stocker de la donnée sous forme de dictionnaire.

Rien a coder, vous pouvez utiliserer Redis comme serveur de données, lancé dans un conteneur sur votre machine. Accessible une fois lancer via `localhost` sur le port `6379`.

Dans un autre terminal vous pouvez lancer `redis` frontalement via la commande :

```bash
docker run --name myredis --rm -p 6379:6379 redis
```

> [!tip]
> Utilisez l'outil `redis-cli` pour accéder à `redis` directement sans script `python`. (c.f. [Installer Redis](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/))

Si vous stockiez vos users, communications et incidents dans des variables dictionnaires locales, vous pouvez maintenant la remplacer par un stockage dans le serveur `redis`.

#### Exemple: stocker les users, incidents via Redis

Vous pouvez stocker dans plusieurs bases Redis.

Une base contenant les .

*Exemple :* `key=INC-timestamp, value=’{“source”: “username”, “duree”: ”YYYY.MM.DD.HH.MM.SS”, “titre”: ”titre”, "description": "incident à fort impact"}’`

Une base contenant les utilisateurs dans laquelle la clé sera le nom d’utilisateur et en valeur la liste des clés de ses incidents suivis.

*Exemple :* `key=username, value=[INC-timestamp_1, INC-timestamp_2, INC-timestamp_3]`

L'architecture ci-dessus est un exemple. Vous êtes libre de choisir une autre architecture, mais elle doit fonctionner 😉

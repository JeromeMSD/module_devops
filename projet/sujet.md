[![uB](img/UB.png)](https://u-bourgogne.fr/) | ESIREM - 4A - ILIA <br/> DevOps <br/><br/> **[ EXAMEN PRATIQUE ]** | [![ESIREM](img/ESIREM.png)](https://esirem.u-bourgogne.fr/)
:--- |:------------------------------------------------------------------:| ---:
||                  ||

# Sujet projet - Année 2024/2025

> [!warning]
> Avant de commencer, veiller à prendre connaissance des attentes projet [./README.md#exigences-du-projet](./README.md#exigences-du-projet).

Ce projet est à rendre au plus tard le `Jeudi 16 Janvier 2025 à 23h59`. À partir de cette date, aucun changement (commit, issue ou pull_request) ne sera pris en compte pour la notation.

[![Twitter](https://f.hellowork.com/blogdumoderateur/2023/07/X-Twitter-Logo-origine.jpg)](https://x.com)

<br/>

Au cours de ce projet, nous allons réaliser les différentes composantes microservices permettant de refaire le SaaS **X ( ancien Twitter )** ☝️

## Polytex 🚀

Concevoir une grappe de microservice composée d'API simples `Python/Flask` et d'un frontend. Cet ensemble permettra de répondre aux fonctionnalités suivantes :

* Twetter & retweeter.
* Liker & commenter des tweets.
* Afficher tous les tweets.
* Afficher les tweets liés à une personne.
* Créer, modifier un profil utilisateur.
* Afficher les sujets (hashtag).
* Afficher les tweets liés à un sujet (hashtag).
* Envoyer des messages privés à un autre utilisateur.

Via la déclaration de route `GET` et `POST` vous définirez les fonctions pour répondre aux fonctionnalités si dessus ☝️

**Polytex** sera composé d'au moins 4 microservice. 

- Gestion des profils utilisateurs (CRUD) et identité.
- Gestion des messages privés (entre 2 personnes ou plus).
- Gestion des tweets (tweets & retweets, recherche & hashtags).
- Gestion des réactions (likes, commentaire).
- Frontend

> [!note]
> Chacun des microservices et le frontend feront l'objet d'un dossier dans le dépôt. (cf. [./README.md#exigences-du-projet](./README.md#exigences-du-projet))

### Gestion des hashtags

Gérer les sujets peut se faire en créant une clé dédiée au sujet dans le dictionnaire des utilisateurs.

*Par exemple* : Vous pouvez utiliser un préfix pour éviter les conflits de clé. Par exemple, les utilisateurs auront une clé au format `u-username` et les sujets `h-hashtag`.

> **[ Tips ]** Pour trier les liens entre sujets, utilisateurs et tweets tout se fera au traitement de la requête.

ℹ️ vous pouvez utilisez un autre format, votre choix est à préciser dans le readme.

### Gestion des objets

L'envoie et le retour de données dans les requêtes et les reponses `HTTP` peut être simplifié via l'utilisation de structure [`JSON`](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation). Vous pourrez gérer vos traitements et/ou transformation de donnée ou de message dans les routes de votre API.

> [!tip]
> Avant de mettre en place les bases Redis, vous pouvez utiliser des dictionnaires pour tester vos routes et vos fonctionnalités.

Testez vos routes avec la commande `curl`.

### Stockage

Pour externaliser le stockage des données et garantir leurs conservations en cas redémarrage des microservices, le tout dans une base rapide et sans contrainte, vous pouvez utiliser `redis`.

> [!important]
> Vous êtes libre de choisir le découpage pour le stockage, échanger autour des possibilités et documenter les via issues et fichier Markdown.

#### Qu'est ce que Redis ? (rappel) 

`Redis` est une base de donnée clé/valeur qui vous permettra de stocker de la donnée sous forme de dictionnaire.

Vous utiliserez Redis comme serveur de données, lancé dans un conteneur sur votre machine. Accessible une fois lancer via `localhost` sur le port `6379`.

Dans un autre terminal vous pouvez lancer `redis` frontalement via la commande :

```bash
docker run --name myredis --rm -p 6379:6379 redis
```

> [!tip]
> Utilisez l'outil `redis-cli` pour accéder à `redis` directement sans script `python`.

Si vous stockiez vos tweets dans une variable dictionnaire vous pouvez maintenant la remplacer par un stockage dans le serveur `redis`.

#### Exemple: stocker les tweets via Redis

Vous pouvez stocker dans plusieurs bases Redis.

Une base contenant les tweets.

*Exemple :* `key=timestamp, value=’{“author”: “username”, “tweet”: ”message”}’`

Une base contenant les utilisateurs dans laquelle la clé sera le nom d’utilisateur et en valeur la liste des clés de ses tweets.

*Exemple :* `key=username, value=[timestamp_1, timestamp_2, timestamp_3]`

L'architecture ci-dessus est un exemple. Vous êtes libre de choisir une autre architecture, mais elle doit fonctionner 😉

---

## Base choisie lors du CM3

> TO DO

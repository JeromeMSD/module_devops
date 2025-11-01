| [![uB](https://upload.wikimedia.org/wikipedia/fr/c/cc/Logo_EPE_Universit%C3%A9_Bourgogne_Europe.svg)](https://u-bourgogne.fr/) | Polytech Dijon - 4A - ILIA - DevOps <br/><br/> **[ EXAMEN PRATIQUE ]** | [![ESIREM](https://polytech.ube.fr/wp-content/uploads/2023/02/Logo_Reseau_Polytech.svg_-300x191.png)](https://esirem.u-bourgogne.fr/) |
|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                |                                                                        |                                                                                                                                       |

# Sujet projet - Année 2025

> [!warning]
> Avant de commencer, veiller à prendre connaissance des attentes projet [./README.md#exigences-du-projet](./README.md#exigences-du-projet).

Ce projet est à rendre au plus tard le `Vendred 14 novembre 2025 à 23h59`. À partir de cette date, aucun changement (commit, issue ou pull_request) ne sera pris en compte pour la notation.

![PolyStatus](https://github.com/user-attachments/assets/ad8a7ec4-eb29-4ac4-ab15-2f6513b8f4f1)

<br/>

Au cours de ce projet, nous allons réaliser les différentes composantes microservices de suivi d'incident, comme le fait par exemple [DownDetector](https://downdetector.fr/).

## PolyStatus 🚀

Concevoir une grappe de microservice composée d'API simples `Python/Flask` et d'un frontend. Cet ensemble permettra de répondre aux fonctionnalités suivantes :

- **Permettre le suivi d'incident** — création, suivi, timeline, changement de statut, assignation et postmortem détaillé.
- **Gérer différent type d'utilisateurs et des SREs** pour permettre d'attribuer les actions à réaliser, les référents des incidents.
- Récupérer les status officiels et annonces des fournisseurs, voir les liens de cause à effet entre les différents providers.
- **Surveillance automatique** des status pages cloud (AWS, GCP, Cloudflare…) et création d’incidents à partir de ces sources.

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

### Détails d'implémentation

#### Routes par microservice

Afin de permettre aux différents microservices de communiquer entre eux, nous allons définir des standards. Standards qui
permettront de savoir comment appeler chaque microservice et quel sera le format de la réponse reçue.
Ces standards devront, pour chaque microservice, être répertorié dans un fichier `swagger.yaml`.

#### Gestion des objets (API REST et JSON)

L'envoie et le retour de données dans les requêtes et les reponses `HTTP` peut être simplifié via l'utilisation de structure [`JSON`](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation). Vous pourrez gérer vos traitements et/ou transformation de donnée ou de message dans les routes de votre API.

> [!tip]
> Avant de mettre en place les bases Redis, vous pouvez utiliser des dictionnaires en variables locales dans le microservice pour tester vos routes et vos fonctionnalités.

Testez vos routes avec la commande `curl`.

> [!note]
> Gardez en tête l'objectif d'autonomie des microservices, l'idée est de créer des [API REST ](https://www.redhat.com/fr/topics/api/what-is-a-rest-api).

#### Exemple de route

Pour des **exemples** de routes définit comme suit, vous trouverez un **exemple** de swagger associé.

> [!caution]
> Le fichier `swagger.yaml` doit être à jour en tout temps, pour permettre aux autres équipes de savoir comment requêter votre API.

**users**

| Route                     | Action                                            | Reponse                                                 |
|---------------------------|---------------------------------------------------|---------------------------------------------------------|
| `POST /api/v1/users`      | Permet de créer un utilisateur.                   | Retourne un HTTP code de succès (HTTP 200). (si succès) |
| `POST /api/v1/auth/login` | Permet la connection de l'utilisateur.            | Retourne un token.                                      |
| `GET /api/v1/users`       | Permet de récupérer la liste des utilisateurs.    | Retourne une liste.                                     |
| `GET /api/v1/users/<id>`  | Permet de récupérer les détails d'un utilisateur. | Retourne un objet JSON représentant un utilisateur.     |
| `PUT /api/v1/users/<id>`  | Permet de modifier les détails d'un utilisateur.  | Retourne un HTTP code de succès.                        |

> Exemple de swagger pour le microservice utilisateurs: [./swaggers/users.yaml](./swaggers/users.yaml)

**incidents**

| **Route / Endpoint**                     | **Action**                                                                            | **Réponse**                                             |
|------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------|
| `POST /api/v1/incidents`                 | Créer un nouvel incident                                                              | Retourne un **objet JSON** représentant l’incident créé |
| `GET /api/v1/incidents`                  | Lister les incidents                                                                  | Retourne une **liste JSON** d’incidents                 |
| `GET /api/v1/incidents/<id>`             | Récupérer les détails d’un incident par id                                            | Retourne un **objet JSON** représentant l’incident      |
| `POST /api/v1/incidents/<id>/assign`     | Assigner un incident                                                                  | Retourne l’incident mis à jour                          |
| `POST /api/v1/incidents/<id>/status`     | Mettre à jour le **statut** d’un incident (`open`, `mitigated`, `resolved`)           | Retourne l’incident avec son nouveau statut             |
| `POST /api/v1/incidents/<id>/timeline`   | Ajouter un **événement** dans la timeline (note, mise à jour, mitigation, résolution) | Retourne un code HTTP 200  (si succès)                  |
| `POST /api/v1/incidents/<id>/postmortem` | Soumettre ou modifier le **postmortem** d’un incident                                 | Retourne un code HTTP 200 (si succès)                   |

> Exemple de swagger pour le microservice d'incident: [./swaggers/incidents.yaml](./swaggers/incidents.yaml)

**communication**

| **Route / Endpoint**               | **Action**                                                                              | **Réponse**                                                                               |
| ---------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `POST /api/v1/public/announce`     | Publier une **annonce publique** liée à un incident (message et état)                   | Retourne un **objet JSON** représentant l’annonce créée (**HTTP 201**)                    |
| `GET /api/v1/public/status`        | Récupérer le **statut public** global (incidents en cours ou récents)                   | Retourne une **liste JSON** d’incidents publics et leurs derniers messages (**HTTP 200**) |
| `POST /api/v1/subscriptions/email` | Ajouter une **adresse email** à la liste des abonnés pour recevoir les annonces         | Retourne un **code HTTP 201** (succès de l’abonnement)                                    |
| `POST /api/v1/webhooks`            | Enregistrer un **webhook** pour notifier un système externe lors de nouveaux événements | Retourne un **code HTTP 201** (webhook enregistré avec succès)                            |

> Exemple de swagger pour le microservice de communications: [./swaggers/comms.yaml](./swaggers/comms.yaml)

**csp-ingestor**

| **Route / Endpoint**                           | **Action**                                                                         | **Réponse**                                                            |
|------------------------------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| `POST /api/v1/csp/providers`                   | Ajouter un **fournisseur cloud** (CSP) à surveiller, avec son flux de statut       |  Retourne un **code HTTP 201** confirmant l’enregistrement du provider |
| `POST /api/v1/csp/refresh?provider=cloudflare` | Rafraîchir manuellement les **événements de statut** pour un provider donné        | Retourne un **objet JSON** avec le résultat du rafraîchissement        |
| `GET /api/v1/csp/events?active=true`           | Récupérer la liste des **incidents actifs détectés** chez les fournisseurs CSP     | Retourne une **liste JSON** d’événements                               |
| `POST /api/v1/incidents`                       | Création d’un incident interne lorsqu’un événement critique est détecté sur un CSP | Retourne un **objet JSON** de l’incident créé avec le champ            |

> Exemple de swagger pour le microservice csp-ingestor: [./swaggers/csp.yaml](./swaggers/csp.yaml)

**flags**

| **Route / Endpoint**                 | **Action**                                                                             | **Réponse**                                                                                          |
|--------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `GET /flags?user=<user>&role=<role>` | Récupérer la liste des **feature flags** applicables à un utilisateur selon son rôle   | Retourne un **objet JSON** contenant les flags et leurs variations                                   |
| `GET /admin/flags`                   | Récupérer la liste des **feature flag**  existant                                      | Retourne la liste des features flags existants                                                       |
| `GET /admin/flags`                   | Récupérer la liste des **feature flag**  existant                                      | Retourne un objets avec des listes des features flags activés par un utilisateur et/ou par un groupe |
| `POST /admin/flags/`                 | Créer ou mettre à jour un **feature flag**                                             | Retourne un **code HTTP 201** ou **200** selon la création ou la mise à jour                         |
| `POST /admin/toggle/<key>`           | Activer ou désactiver un **feature flag** existant                                     | Retourne un **code HTTP 200** (si succès de la modification)                                         |

> Exemple de swagger pour le microservice de feature flags: [./swaggers/flags.yaml](./swaggers/flags.yaml)

> [!tip]
> Le YAML n'est pas clair ? Vous pouvez le passer dans https://editor.swagger.io

---

### Informations fonctionnelles

#### Annonces

Les annonces seront majoritairement gérées au niveau de l'application mais vous pouvez mettre en place une interconnection avec un service SMTP.

#### CSP-ingestor

L'ingestion des informations des Cloud Service Provider peut se faire par scrapping de site web, mais je vous recommande d'intégrer dans un premier temps les CSP qui propose une APIs d'incident.

- https://www.cloudflarestatus.com/api
- https://www.githubstatus.com/api
- https://status.cloud.google.com/incidents.json
- https://status.atlassian.com/api

Autre page à intégrer: [AWS](https://health.aws.amazon.com/health/status), [GitLab](https://status.gitlab.com/), [Docker](https://www.dockerstatus.com/).
Ou toute autre application de votre choix ! 🚀

> [!tip]
> Vous pouvez aussi mettre en place de l'intégration de flux RSS.
> 
> Si votre application préférée ne propose pas de status page, vous pouvez faire un appel HTTP pour confirmer leur disponibilité !

---

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

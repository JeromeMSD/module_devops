# TP Projet

Le projet noté du module de DevOps évaluera compétences et bonnes pratiques de développement vues en cours. La notation tiendra compte des fonctionnalités déployées dans l’API, de la bonne mise en place des points d’exigences projets ainsi que de la collaboration entre les membres du groupe.

Il n'y a pas de rapport, le (ou les) `README.md`  de votre dépôt remplira cette fonction, soignez leur rédaction et faites qu'ils soient le plus complet possible.

**Bon courage 🚀**

___

## Sujet 

> [!note]
> WIP

## Exigences du projet

Pour réaliser le projet vous disposer des deux dernières séances de TDs et du projet GitHub suivant: https://github.com/JeromeMSD/projet_devops-ilia-2024-5.

> [!important]
> Fin du projet le `Jeudi 16 Janvier 2025 à 23h59`.

Le but de ce projet est de vous faire travailler ensemble sur un même objectif.
L’historique des changements sur le dépôt devra donc montrer la collaboration entre les membres du groupe (changement de sources différentes).

> [!important]
> Toute modification apportée à la branche principale du projet doit l'être via [Pull Request](https://docs.github.com/fr/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

### Documentations

Le projet sera à documenter via fichiers Markdown, issues et swagger. Son architecture de fichier devrait, à terme, ressembler à ce quit suit.

```
./
├── .gitignore
├── .github/
│   └── workflows/
│   │   └── workflow-1.yml
│   │   └── workflow-2.yml
│   │   └── ...
│   │   └── workflow-x.yml
├── docs/
│   ├── nom-du-microservice/
│   │   ├── index.md
│   │   └── autres-fichiers-de-documentation.yml
│   ├── ...
│   ├── index.md
│   ├── installation.md
│   └── autres-fichiers-de-documentation.yml
├── nom-microservice/
│   └── src/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── utils.py
│   │   └── models/
│   │       ├── __init__.py
│   │       └── example_model.py
│   └── tests/
│   │   ├── __init__.py
│   │   ├── test_main.py
│   │   └── test_utils.py
│   └── data/
│   │   ├── fichier-1.csv
│   │   ├── ...
│   │   └── fichier-x.csv 
│   ├── requirements.txt
│   ├── README.md
│   └── swagger.yaml
├── ...
├── README.md
└── CONTRIBUTING.md
```

Correspondant aux choses suivantes :

- `.gitignore`: Liste des fichiers à exclure du contrôle de version. (fourni)
- `.github/`: Contient les configurations pour GitHub, comme les workflows d'intégration continue.
- `docs/`: Contient la documentation [Markdown](https://www.markdownguide.org/basic-syntax/) principale du projet. (avec un sous-dossier pour chaque microservice)
- `nom-microservice/`: Le dossier d'un microservice, avec:
  - `src/`: Code source du microservice.
  - `tests/`: Tests unitaires et fonctionnels du microservice.
  - `data/`: Contient les fichiers à importer dans le microservice en exécution pour peupler le ou les schémas de données. (si nécessaire).
  - `requirements.txt`: Dépendances nécessaires pour exécuter le microservice.
  - `README.md`: Documentation du microservice.
  - `swagger.yaml`: Contient la description des routes & fonctions associées disponibles dans le microservice.
- `README.md`: README global avec introduction au projet, des instructions d'installation et d'utilisation.
- `CONTRIBUTING.md`: Guide pour contribuer au projet.

> [!important]
> Le `README.md` global doit également contenir un tableau (en MarkDown évidemment) ou chacun des contributeurs viendra ajouter **nom**, **prénom**, **pseudo GitHub** et **lien vers son profil GitHub**.

#### Les microservices se doivent d'avoir une API stable et bien documenter !
Chacun des microservices du projet devra être documenté **a minima d'un README et d'un Swagger**.

> [!tip]
> Le Swagger est un fichier YAML qui décrit les différentes routes REST disponible via requêtes HTTP au sein d'une API.
> 
> Utiliser https://editor.swagger.io/ pour décrire les routes de votre microservice et enregistrer le contenu dans un fichier `swagger.yaml`.

### Github Actions

Différentes GitHub Actions devront venir automatiser le projet. Sont attendues a minima les GitHub Actions suivante:

* `lint` sur les `pull_request`.
* CI de build pour chacun des microservices.
* 

### Pull requests

Chaque ajout de fonctionnalité, correction **ou** refactorisation devra faire l'objet d'une [Pull Request](https://docs.github.com/fr/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).
Cette PR devra être revue par **au moins 3 autres collaborateurs du projet**.

### Issues

Pour discuter et débattre autour d'une fonctionnalité, amélioration ou correction de bug, utiliser les [issues](https://docs.github.com/fr/issues/tracking-your-work-with-issues/about-issues).

Les commentaires des issues utilisent le [Markdown](https://www.markdownguide.org/basic-syntax/). 
Pensez à vous en servir pour mettre en valeur informations et bloc de code ! 🚀

> [!tip]
> Utiliser les `labels` pour faciliter le triage des issues (peut également être utilisé pour les PRs).

### Docker

Pour chacun des microservices, un fichier `Dockerfile` permettant de conteneuriser le programme est attendu. 

- Le conteneur doit présenter le moins de vulnérabilité possible.
- Le résultat de la dernière analyse `trivy` est attendue dans le `README.md` du microservice.
- Une image du conteneur du microservice doit être présente sur le registre Artifact Registry.
    > format `europe-west1-docker.pkg.dev/polytech-dijon/polytech-dijon/ms-<nom du microservice>:<version>`
- Une GitHub Action permettant le `build & push` l'image du conteneur automatiquement vers ce registre.

> [!important]
> La présence d'un fichier `compose.yaml` fonctionnel dans les dossiers des microservices est facultative mais sera valorisée.

## Notation

Il y a de nombreuses façons d'apporter de la valeur à ce type de projet.
Vous serez noté individuellement sur votre participation au projet à travers les axes suivants:

- Implémentation des fonctionnalités des microservices.
- Amélioration des microservices et du projet.
- Conteneurisation des microservices.
- Revue de code.
- Intégration continue & automatisation (via Github Actions).
- Collaboration autour des microservices au sein du projet (via les issues, pull_requests).
- Documentation des microservices et du projet (via les `README.md` & `swagger.yaml`).

> [!tip]
> L'utilisation de bonnes pratiques DevOps, de Test Driven Development ainsi que toutes les explorations & implémentations documentées pourront être valorisées. 
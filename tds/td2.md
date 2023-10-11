# TD n°2 : Git & Github Action

Dans ce TD, vous allez apprendre à manipuler une dépôt de code source avec l'outil Git :

* Créer un dépôt sur GitHub
* Documenter un dépôt via `README.md`
* Créer des GitHub actions dans le dossier `.github/workflows/*.yaml`

Le but est de vous faire collaborer dans la réalisation de ce TD et des suivants. L’équité des modifications sur le dépôt font partie de la note.

## Poser les bases du projet.

> Pour commencer à collaborer, il nous faut un dépôt !

Créez un nouveau dépôt **publique** sur le GitHub d’un des membres du binôme :

1. L’heure du choix le plus difficile, celui du nom ! Choisissez un nom pour votre dépôt, soyez créatif ce dépôt va accueillir le projet !
( pas de panique, vous pourrez changer le nom plus tard si vous en ressentez le besoin dans les paramètres du dépôt ). Ce nom doit être spécifié en snake_case et devra être préfixé avec `4A_[ ILC ou SQR ]_`
2. Ajoutez le second membre du binôme en tant que collaborateur.
3. Ajoutez-moi en tant que collaborateur. `jerome.massard@kiowy.com`


## Documenter le dépôt

Maintenant, initions les bonnes pratiques :

1. Créer un fichier README.md à la racine du projet.
2. Rédiger une première ébauche de README dans ce fichier avec :

* Les prénoms et noms de chacun d’entre vous
* Votre spécialité ( ILC ou SQR )
* Différentes sections et sous-sections pour chacun des exercices.
* Un lien vers votre compte GitHub.
* Insérer une image via ! en donnant le lien vers l’image de votre choix.
* Terminer par une sections de premier niveau ( hors titre ) “Statuts actions” 

Besoins d’aides ? 

→ [Documentation README/Markdown](https://www.makeareadme.com/)

→ [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

## Automatiser votre dépôt

Implémenter et tester dans le dossier `./github/workflows/` :

* Une action qui se déclenche à **chaque push** pour exécuter echo "New push !"
* Une action qui se déclenche **sur commande manuel** pour exécuter une commande curl sur l’adresse `wttr.in/Moon` via une Action du marketplace
* Une action nommé `Hello PR` qui se déclenche à **chaque Pull Request** avec un job `build`

### Étape du job `build`
1. Utiliser actions/checkout@v3 ( pour accéder au code )
2. Utiliser actions/setup-python@v4 ( pour installer python )
3. Exécuter la commande python main.py
4. Créer un script python pour écrire sur la sortie standard “Hello there !”

### Tips
- Utilisez l’éditeur d’action dans GitHub.
- Aidez-vous du marketplace Github Action à droite de l’éditeur dans GitHub.

### Validation

Pour finir, utiliser les **issues** GitHub pour me communiquer que vous avez terminé ce TPs en créer une issue de type `documentation` sur ce dépôt [JeromeMSD/module_ci-cd](https://github.com/JeromeMSD/module_ci-cd).

# TD n°3 - Conteneurisation ++

> [!warning]
> En cours de construction

## Sécurité des conteneurs

### Trivy

[Trivy](https://github.com/aquasecurity/trivy) est un outil de scan d'image qui permet d'identifier les vulnérabilités d'une configuration.

En vous basant sur [la documentation de l'outil](https://trivy.dev/v0.57/getting-started/installation/), installer l'outil en suivant les étapes recommandées pour votre système.

Tryvi s'utilise sur des configurations (Kubernetes, Terraform, etc) et des images en suivant le format de commande suivant:

```bash
trivy <target> [--scanners <scanner1,scanner2>] <subject>
```

Nous allons scanner notre première image, utiliser `trivy` pour scanner l'image `python:3.4-alpine`.

```bash
trivy image python:3.4-alpine
```

**Que pouvez-vous observer ?**

Nous allons maintenant scanner les images construites dans la parties précédentes.

1. Construiser les images de conteneur `frontend` et `backend` à partir des procédures précédentes et scanner ces images.
2. Résolver les vulnérabilités identifiées par `trivy`.
3. Reconstruiser et rescanner vos images, si des vulnérabilités sont listées, reprennez **à l'étape 2**.

**Un dernier test pour la route**

Scanner l'ensemble des fichiers du dossier de votre dépôt en local avec `trivy`.

> [!tip]
> Un ensemble de fichiers et de dossiers avec une racine commune est aussi appelé "système de fichier" qui se traduit par "File System" en anglais et s'abrège `fs`.

#### Bonus - Tout ça en plus simple

Trivy dispose d'une GitHub Action ! Via les informations de [ce dépôt](https://github.com/aquasecurity/trivy-action) et le Market Place des GitHub Action. Mettez en place sur votre dépôt une GitHub Action qui scan les images issues de vos Dockerfiles.

### Falco

[Falco](https://falco.org/) est un outil de sécurité Cloud Natif qui assure la sécurité à l'exécution des machines hôtes, des conteneurs, de Kubernetes, des environnements Cloud. C'est un outil actif qui surveille l'environnement dans lequel il est déployé en temps réel.

Pour ce faire, Falco utilise le concept de **règle**. Chaque règle décrit un comportement à risque et le niveau de criticité associé à ce comportement. Si un de ces comportements est observé, Falco l'enregistre sous la forme d'évenement.

Falco a été installé au sein du cluster Kubernetes que nous avons utilisé durant le module de **Virtualisation & Cloud Computing**.

Nous allons commencer par tester la configuration par défaut de Falco.

1. Connectez-vous au cluster.
2. Créer un déploiement pour une Pod exécutant l'image `nginx`.

    ```shell
    kubectl create deployment nginx --image=nginx
    ```

3. Executons maintenant dans ce pod, un comportement suspect:

    ```shell
    kubectl exec -it $(kubectl get pods --selector=app=nginx -o name) -- cat /etc/shadow
    ```

    > [!info]
    > Cette commande tente d'afficher le contenu du fichier `shadow` stocker dans le dossier `/etc/` du conteneur exécuté (dossier administrateur).

4. Que pouvez-vous observé dans les logs de Falco ? (affichage des evenements de type `Warning`)

    ```shell
    kubectl logs -l app.kubernetes.io/name=falco -n falco -c falco | grep Warning
    ```

> [!tip]
> **Félicitation !** Vous avez pu observer votre premier évènement de sécurité avec [Falco](https://falco.org/).
>
> Curieux de savoir quelle était cette règle qui a été enfreinte ? Sa description est [ici](https://github.com/falcosecurity/rules/blob/c0a9bf17d5451340ab8a497efae1b8a8bd95adcb/rules/falco_rules.yaml#L398).




Now it's time to create our own rule and load it into Falco. We can be pretty creative with them, but let's stick with something simple. This time, we want to be alerted when any file is opened for writing in the /etc directory, either on the host or inside containers.

1. Créer un fichier `my-falco-rule.yaml` à partir du contenu suivant :

```yaml
customRules:
  custom-rules.yaml: |-
    - rule: Write below etc
      desc: An attempt to write to /etc directory
      condition: >
        (evt.type in (open,openat,openat2) and evt.is_open_write=true and fd.typechar='f' and fd.num>=0)
        and fd.name startswith /etc
      output: "File below /etc opened for writing (file=%fd.name pcmdline=%proc.pcmdline gparent=%proc.aname[2] ggparent=%proc.aname[3] gggparent=%proc.aname[4] evt_type=%evt.type user=%user.name user_uid=%user.uid user_loginuid=%user.loginuid process=%proc.name proc_exepath=%proc.exepath parent=%proc.pname command=%proc.cmdline terminal=%proc.tty %container.info)"
      priority: WARNING
      tags: [filesystem, mitre_persistence]    
```

2. Charger la règle dans l'instance de Falco en exécution dans le cluster.

    ```shell
    helm upgrade --namespace falco falco falcosecurity/falco --set tty=true -f falco_custom_rules_cm.yaml
    ```

    > [!note]
    > `helm` est un outil pour faciliter la manipulation de manifest `yaml`. [Installer HELM](https://helm.sh/fr/docs/intro/install/)

3. Attendez que l'instance de Falco est redémarré avec la nouvelle règle.

    ```shell
    kubectl wait pods --for=condition=Ready --all -n falco
    ```

4. Tester votre règle.

    ```shell
    kubectl exec -it $(kubectl get pods --selector=app=nginx -o name) -- touch /etc/test_file_for_falco_rule
    ```

    ```shell
    kubectl logs -l app.kubernetes.io/name=falco -n falco -c falco | grep Warning
    ```

> [!tip]
> **Vous avez créer votre première règle Falco 🚀**

## Bonus - Accéder à l'interface pour lire les évènements

Falco possède un projet annexe nommé **Falcosidekick**, offrant une interface utilisateur pour la lecture des évènements. **Falcosidekick** et **Falcosidekick UI** ont été ajouté au cluster.

1. Utiliser le `port-forward` pour créer un tunnel entre votre machine et le service **Falcosidekick UI**.

```shell
kubectl get -n falco service
```
```shell
kubectl -n falco port-forward svc/falco-falcosidekick-ui 2802
```

2. Accéder à l'interface via votre navigateur préféré en vous rendant sur http://localhost:2802/
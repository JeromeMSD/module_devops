# TD n°4 - Build via docker

Utilisez docker pour build votre application, comme sur votre pc.

Quelques rappels :

* Un container à besoin d’une image de base

<details>
	<summary>aide</summary>
	<p>
	→ la plus petite possible ( pour la légèreté ) python:3.8
	</p>
</details>

* Le container est un env. indépendant

<details>
	<summary>aide</summary>
	<p>
	→ Il faut installer Flask
	→ Mettre en place les bonnes variables d'environnement
	→ Il faut exposer le port de Flask
	</p>
</details>

* Un container à besoin d’un point d’entrée

<details>
	<summary>aide</summary>
	CMD ["flask", "run"]
</details>
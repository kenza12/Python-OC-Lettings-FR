
.. OC Lettings documentation master file, created by
   sphinx-quickstart on Sat Aug  3 21:13:30 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation de OC Lettings
============================

Bienvenue dans la documentation de OC Lettings. Ce document décrit les aspects techniques du projet, y compris l'installation, le démarrage rapide, les technologies utilisées, la structure de la base de données, les interfaces de programmation, les cas d'utilisation, et les procédures de déploiement et de gestion de l'application.

.. toctree::
   :maxdepth: 2
   :caption: Contenu:

   Description du projet <description_projet>
   Installation <installation>
   Demarrage Rapide <demarrage_rapide>
   Technologies <technologies>
   Base de Donnees <base_donnees>
   Interfaces <interfaces>
   Utilisation <utilisation>
   Deploiement <deploiement>

Description du projet
=====================

Le projet OC Lettings est une application web permettant la gestion de locations et de profils utilisateurs. Développé avec Django, il propose une interface simple pour afficher et gérer les informations des locations et des utilisateurs.

Des améliorations ont été apportées pour optimiser l'architecture, résoudre des problèmes, surveiller l'application et automatiser le déploiement.

1. **Amélioration de l’architecture modulaire** :
    - Le code a été réorganisé en applications distinctes pour une meilleure modularité.

2. **Réduction de divers problèmes sur le projet** :
    - Les problèmes existants ont été résolus pour améliorer la qualité et la stabilité de l'application.

3. **Surveillance de l’application et suivi des erreurs via Sentry** :
    - Sentry a été installé et configuré pour surveiller et gérer les erreurs de manière efficace.

4. **Pipeline CI/CD et le déploiement** :
    - Un pipeline CI/CD complet a été mis en place pour automatiser la compilation, les tests, la conteneurisation et le déploiement du site en production.

5. **Documentation de l’application** :
    - Une documentation technique a été créée pour décrire les aspects du projet, y compris l'installation, les technologies, la structure de la base de données et les procédures de déploiement.

Installation
============

Pour installer le projet OC Lettings, vous aurez besoin de :

- Python 3.11 ou plus
- Un compte GitHub avec les secrets définis
- Un compte AWS configuré pour le déploiement
- Un compte DockerHub

Ensuite, veuillez suivre les étapes ci-dessous :

**1. Clonez le dépôt depuis GitHub :**
   
.. code-block:: bash

   git clone https://github.com/kenza12/Python-OC-Lettings-FR.git

**2. Accédez au répertoire du projet :**

.. code-block:: bash

   cd Python-OC-Lettings-FR

**3. Créez et activez un environnement virtuel :**

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\Activate.ps1`

**4. Installez les dépendances :**

.. code-block:: bash

   pip install -r requirements.txt

Demarrage Rapide
================

Pour démarrer rapidement avec OC Lettings :

**1. Activez l'environnement virtuel :**

.. code-block:: bash

   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\Activate.ps1`

**2. Exécutez le serveur de développement Django :**

.. code-block:: bash

   python manage.py runserver

**3. Ouvrez votre navigateur et accédez à l'URL suivante :**

.. code-block:: none

   http://localhost:8000

**4. Accédez à l'interface d'administration :**

   Vous pouvez accéder à l'interface d'administration en naviguant à l'URL suivante : http://127.0.0.1:8000/admin/

   Les identifiants de connexion sont :

   - **Nom d'utilisateur** : admin
   - **Mot de passe** : Abc1234!

Technologies
============

Le projet OC Lettings utilise les technologies et langages suivants :

- **Django** : Framework web utilisé pour le développement de l'application.
- **Django-storages** : Facilite le stockage des fichiers statiques sur des services cloud comme AWS S3.
- **boto3** : Bibliothèque AWS SDK pour Python, utilisée pour interagir avec les services AWS, comme S3.
- **SQLite** : Base de données pour stocker les données de l'application.
- **Docker/DockerHub** : Pour la containerisation de l'application, permettant de créer et partager des images Docker.
- **AWS** : Utilisé pour le déploiement de l'application. Les services AWS utilisés incluent :

  - S3 pour le stockage des fichiers statiques
  - EC2 pour l'hébergement des instances de calcul
  - ECS pour l'orchestration des conteneurs Docker
  - ECR pour le stockage des images Docker

- **GitHub/GitHub Actions** : Pour l'hébergement du code source, l'intégration continue, et le déploiement automatisé via des workflows.
- **pytest/pytest-cov** : Framework de test pour écrire et exécuter des tests automatisés, avec une mesure de la couverture de code.
- **Sentry** : Outil de surveillance et de gestion des erreurs en production, intégrant le suivi des exceptions non gérées.
- **flake8** : Outil de linting pour Python, aidant à détecter et corriger les erreurs de style et de syntaxe.

Base de Données
===============

La base de données du projet OC Lettings utilise SQLite et est structurée avec les modèles suivants, regroupés en deux applications distinctes : `profiles` et `lettings`.

Modèles de l'application `profiles`
-----------------------------------

- **User** : Modèle par défaut de Django représentant les utilisateurs.
- **Profile** : Modèle représentant les profils des utilisateurs, avec les champs suivants :

  - `user` : L'utilisateur associé (OneToOneField).
  - `favorite_city` : La ville favorite de l'utilisateur (CharField).

Modèles de l'application `lettings`
-----------------------------------

- **Address** : Modèle représentant une adresse, avec les champs suivants :

  - `number` : Le numéro de la maison (PositiveIntegerField).
  - `street` : Le nom de la rue (CharField).
  - `city` : Le nom de la ville (CharField).
  - `state` : Le code de l'état (CharField, 2 caractères).
  - `zip_code` : Le code postal (PositiveIntegerField).
  - `country_iso_code` : Le code ISO du pays (CharField, 3 caractères).

- **Letting** : Modèle représentant une location associée à une adresse, avec les champs suivants :

  - `title` : Le titre de la location (CharField).
  - `address` : L'adresse associée (OneToOneField).

Les tables générées par ces modèles sont :

- **auth_user** : Table par défaut de Django pour les utilisateurs.
- **profiles_profile** : Table pour les profils des utilisateurs.
- **lettings_address** : Table pour les adresses.
- **lettings_letting** : Table pour les locations.

Ces tables permettent de stocker et de gérer les informations des utilisateurs et des locations dans l'application OC Lettings.

Interfaces
==========

Le projet OC Lettings propose plusieurs interfaces pour gérer les profils et les locations.

Interface d'Administration Django
---------------------------------

L'interface d'administration intégrée de Django permet aux administrateurs de gérer les données de l'application. Les administrateurs peuvent ajouter, consulter, modifier et supprimer des profils et des locations via cette interface.

- URL : /admin/
- Fonctionnalités : CRUD (Create, Read, Update, Delete) pour les modèles Profile, Letting, et Address.

Interface Graphique du Site
---------------------------

L'interface graphique permet aux utilisateurs de visualiser les profils et les locations via des vues spécifiques. Les utilisateurs peuvent naviguer entre les différentes pages du site pour voir les informations disponibles.

- **Page d'accueil** :
    - URL : /
    - Vue : `index` - Cette vue affiche la page d'accueil avec un contenu de bienvenue.

- **Page des Locations** :
    - URL : /lettings/
    - Vue : `lettings_index` - Cette vue récupère et affiche la liste de toutes les locations disponibles.
    - URL : /lettings/<letting_id>/
    - Vue : `letting_detail` - Cette vue affiche les détails d'une location spécifique identifiée par son letting_id.

- **Page des Profils** :
    - URL : /profiles/
    - Vue : `profiles_index` - Cette vue récupère et affiche la liste de tous les profils d'utilisateurs.
    - URL : /profiles/<username>/
    - Vue : `profile_detail` - Cette vue affiche les détails d'un profil utilisateur spécifique identifié par son username.

Utilisation
===========

L'application OC Lettings propose deux interfaces principales pour les utilisateurs : l'interface d'administration et l'interface utilisateur.

Interface d'Administration
--------------------------

L'interface d'administration de Django permet aux administrateurs de gérer les données de l'application. Voici quelques cas d'utilisation typiques :

- **Ajouter une location** : Accédez à la section des locations dans l'interface d'administration, cliquez sur "Ajouter" et remplissez le formulaire avec les détails de la location.
- **Modifier un profil** : Accédez à la section des profils dans l'interface d'administration, sélectionnez un profil, cliquez sur "Modifier" et apportez les modifications nécessaires.
- **Supprimer une adresse** : Accédez à la section des adresses dans l'interface d'administration, sélectionnez l'adresse à supprimer et confirmez la suppression.

Les administrateurs peuvent effectuer des opérations CRUD (Create, Read, Update, Delete) complètes sur les modèles Profile, Letting, et Address via l'interface d'administration.

Interface Utilisateur
---------------------

L'interface utilisateur permet aux utilisateurs de visualiser les profils et les locations disponibles sur le site. Voici quelques cas d'utilisation typiques :

- **Consulter la liste des locations** : Accédez à la page des locations en cliquant sur "Locations" dans la navigation principale. La liste de toutes les locations disponibles sera affichée.
- **Voir les détails d'une location** : Cliquez sur une location spécifique dans la liste pour afficher ses détails complets.
- **Consulter la liste des profils** : Accédez à la page des profils en cliquant sur "Profiles" dans la navigation principale. La liste de tous les profils d'utilisateurs sera affichée.
- **Voir les détails d'un profil** : Cliquez sur un profil spécifique dans la liste pour afficher les détails de l'utilisateur associé.

Deploiement
===========

Pour déployer l'application OC Lettings, suivez les étapes ci-dessous :

1. **Configuration AWS** :

   - Créez un utilisateur IAM avec les permissions nécessaires pour accéder à EC2, ECR, ECS, et S3.
   - Créez un bucket S3 pour stocker les fichiers statiques (en mode production).
   - Créez un dépôt ECR pour stocker vos images Docker.
   - Configurez un cluster ECS pour héberger vos tâches et services Docker.
   - Configurez une définition de tâche ECS pour spécifier les conteneurs Docker à exécuter.
   - Configurez un service ECS pour gérer et équilibrer la charge des conteneurs.

2. **Secrets GitHub** :

   - Définissez les secrets nécessaires dans votre dépôt GitHub : `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_ACCOUNT_ID`, `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `DJANGO_SECRET_KEY`, `SENTRY_DSN`, `AWS_STORAGE_BUCKET_NAME`.

3. **Déploiement via Docker** :

   - Configurez le fichier `.env` avec les variables nécessaires.
   - Utilisez le script `docker_manager.py` pour automatiser le processus de construction, de push et d'exécution de l'image Docker :

.. code-block:: bash

   python docker_manager.py

En suivant ces étapes, vous pourrez déployer l'application OC Lettings localement ou sur AWS en utilisant Docker.

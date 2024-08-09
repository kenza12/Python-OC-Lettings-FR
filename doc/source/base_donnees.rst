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

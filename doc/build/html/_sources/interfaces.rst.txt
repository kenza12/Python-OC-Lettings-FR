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

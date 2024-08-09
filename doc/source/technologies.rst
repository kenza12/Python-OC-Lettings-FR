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

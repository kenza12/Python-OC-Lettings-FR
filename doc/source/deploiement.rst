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

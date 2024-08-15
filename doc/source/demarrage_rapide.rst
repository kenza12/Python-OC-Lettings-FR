Demarrage Rapide
================

Pour démarrer rapidement avec OC Lettings :

**1. Activez l'environnement virtuel :**

.. code-block:: bash

   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\Activate.ps1`

**2. Exécutez le serveur de développement Django :**

Assurez-vous de configurer le fichier `.env` avec les variables nécessaires.

Exemple de fichier `.env`:

.. code-block:: none

   SENTRY_DSN=https://your_sentry_dsn
   DJANGO_LOG_LEVEL=DEBUG
   DJANGO_SECRET_KEY=your_django_secret_key
   AWS_STORAGE_BUCKET_NAME=your_bucket_name
   AWS_ACCESS_KEY_ID=your_access_key_id
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   DEBUG=True
   DOCKER_USERNAME=your_docker_username
   DOCKER_PASSWORD=your_docker_password

**3. Exécutez le serveur de développement Django :**

.. code-block:: bash

   python manage.py runserver

**4. Ouvrez votre navigateur et accédez à l'URL suivante :**

.. code-block:: none

   http://localhost:8000

**5. Accédez à l'interface d'administration :**

   Vous pouvez accéder à l'interface d'administration en naviguant à l'URL suivante : http://127.0.0.1:8000/admin/

   Les identifiants de connexion sont :

   - **Nom d'utilisateur** : admin
   - **Mot de passe** : Abc1234!

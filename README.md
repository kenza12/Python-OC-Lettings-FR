## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Cette section décrit le processus automatisé de déploiement de l'application `oc_lettings_site` en utilisant **GitHub Actions** et **AWS**. Le déploiement comprend la construction d'une image Docker, son push vers Docker Hub, son pull depuis Docker Hub, et enfin son déploiement sur Amazon ECS.

### Configuration requise

#### Configuration AWS

Pour que le déploiement fonctionne correctement, les éléments suivants doivent être configurés sur AWS :

1. **Créer un utilisateur IAM** :
   - Accédez à la console IAM d'AWS et créez un nouvel utilisateur avec les permissions nécessaires pour accéder à EC2, ECR, ECS, et S3.

2. **Créer un Bucket S3** :
   - Allez dans la console S3 et créez un nouveau bucket pour stocker les fichiers statiques de votre application. Notez que lorsque `DEBUG=False` (mode production), les fichiers statiques seront servis depuis le bucket S3.

3. **Créer un dépôt ECR (Elastic Container Registry)** :
   - Allez dans la console ECR et créez un nouveau dépôt pour stocker vos images Docker.

4. **Créer un cluster ECS** :
   - Accédez à la console ECS et créez un nouveau cluster pour héberger vos tâches et services Docker.

5. **Configurer une définition de tâche ECS** :
   - Créez une définition de tâche qui spécifie les conteneurs Docker à exécuter. Assurez-vous que la définition inclut les paramètres appropriés pour tirer les images Docker depuis ECR et inclure les variables d'environnement nécessaires.

6. **Configurer un service ECS** :
   - Configurez un service ECS dans votre cluster pour gérer et équilibrer la charge des conteneurs. Ce service sera responsable de maintenir le nombre souhaité de tâches en cours d'exécution et de distribuer le trafic entre elles.

7. **Configurer une instance EC2 avec une adresse DNS** (si nécessaire) :
   - Si vous souhaitez servir votre application via une instance EC2, assurez-vous que l'instance est configurée avec une adresse DNS publique. Utilisez le fichier `nginx.conf` disponible sur votre dépôt GitHub pour configurer Nginx en tant que proxy inverse pour votre application Django.

#### Secrets GitHub

Assurez-vous que les secrets suivants sont définis dans votre dépôt GitHub :

- `AWS_ACCESS_KEY_ID` : L'ID de clé d'accès AWS de l'utilisateur IAM.
- `AWS_SECRET_ACCESS_KEY` : La clé d'accès secrète AWS de l'utilisateur IAM.
- `AWS_ACCOUNT_ID` : L'ID de compte AWS où vos ressources sont configurées.
- `DOCKER_USERNAME` : Le nom d'utilisateur de votre compte Docker Hub.
- `DOCKER_PASSWORD` : Le mot de passe de votre compte Docker Hub.
- `DJANGO_SECRET_KEY` : La clé secrète utilisée par Django pour diverses opérations cryptographiques.
- `SENTRY_DSN` : L'URL DSN de votre projet Sentry pour le suivi des erreurs.
- `AWS_STORAGE_BUCKET_NAME` : Le nom du bucket S3 utilisé pour stocker les fichiers statiques.

### Étapes de déploiement

1. **Pousser le code vers le dépôt** :
   - Poussez vos modifications de code vers le dépôt.
   - Assurez-vous que votre branche est soit `master` soit une branche de fonctionnalité qui sera fusionnée dans `master`.

2. **Exécution du pipeline** :
   - Le pipeline CI/CD de GitHub Actions est déclenché à chaque push sur n'importe quelle branche et sur les pull requests vers la branche `master`.
   - Le pipeline comprend trois jobs :
     1. **Build and Test** :
        - **Toutes les branches** :
          - Récupère le code.
          - Configure l'environnement Python.
          - Installe les dépendances.
          - Définit les variables d'environnement (DEBUG=True pour les branches autres que master, DEBUG=False pour master).
          - Exécute les tests avec couverture (minimum 80%).
     2. **Containerize** :
        - **Branche master uniquement** (ou pull request vers master) :
          - Nécessite que le job `build-and-test` réussisse.
          - Récupère le code.
          - Crée un fichier `.env` avec les variables d'environnement de production.
          - Configure Docker Buildx pour des builds multi-plateformes (linux, macos).
          - Se connecte à Docker Hub.
          - Construit et pousse l'image Docker vers Docker Hub.
     3. **Deploy** :
        - **Branche master uniquement** (ou pull request vers master) :
          - Nécessite que le job `containerize` réussisse.
          - Configure les identifiants AWS.
          - Crée un dépôt ECR si nécessaire.
          - Se connecte à Amazon ECR.
          - Tire l'image Docker depuis Docker Hub et la pousse vers ECR.
          - Enregistre une nouvelle définition de tâche dans ECS.
          - Déploie la nouvelle définition de tâche sur le service ECS.

3. **Vérification post-déploiement** :
   - Vérifiez le déploiement en accédant au service ECS.
   - Assurez-vous que l'application fonctionne correctement et sert les fichiers statiques comme prévu.

### Déploiement via Docker uniquement

Pour déployer l'application localement en utilisant Docker, vous pouvez utiliser le script `docker_manager.py`. Assurez-vous de configurer le fichier `.env` avec les variables nécessaires (similaires à celles mentionnées dans la section des secrets GitHub).

*Exemple de fichier `.env`:*

```plaintext
SENTRY_DSN=https://your_sentry_dsn
DJANGO_LOG_LEVEL=DEBUG
DJANGO_SECRET_KEY=your_django_secret_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
DEBUG=True
DOCKER_USERNAME=your_docker_username
DOCKER_PASSWORD=your_docker_password
```

Lancez le script `docker_manager.py` pour automatiser le processus de construction, de push et d'exécution de l'image Docker :

  ```sh
  python docker_manager.py
  ```

En suivant ces étapes, vous pourrez déployer l'application localement en utilisant Docker.

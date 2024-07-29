# Utilisez l'image officielle de Python comme base
FROM python:3.11-slim

# Installer Nginx
RUN apt-get update && apt-get install -y nginx

# Définir les arguments de construction pour les variables d'environnement
ARG AWS_STORAGE_BUCKET_NAME
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG DEBUG

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --upgrade pip && pip install -r requirements.txt

# Installer gunicorn
RUN pip install gunicorn

# Copier le reste du code de l'application dans le conteneur
COPY . .

# Copier le fichier de configuration Nginx dans le conteneur
COPY nginx.conf /etc/nginx/sites-available/default

# Créer un lien symbolique pour activer la configuration Nginx
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Définir les variables d'environnement pour la production
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Définir les variables d'environnement pour S3
ENV AWS_STORAGE_BUCKET_NAME=$AWS_STORAGE_BUCKET_NAME
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV DEBUG=$DEBUG

# Ajouter étape de débogage pour vérifier les variables d'environnement
RUN echo "AWS_STORAGE_BUCKET_NAME=$AWS_STORAGE_BUCKET_NAME"
RUN echo "AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID"
RUN echo "AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY"
RUN echo "DEBUG=$DEBUG"

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer les ports sur lesquels Nginx et l'application Django s'exécutent
EXPOSE 80 8000

# Commande pour lancer Nginx et Gunicorn
CMD service nginx start && gunicorn --bind 0.0.0.0:8000 oc_lettings_site.wsgi:application

# Utilisez l'image officielle de Python comme base
FROM python:3.11-slim

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

# Définir les variables d'environnement pour la production
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port sur lequel l'application s'exécute
EXPOSE 8000

# Lancer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]

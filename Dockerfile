FROM python:3.11-slim

# Install Nginx to act as a reverse proxy for Gunicorn
RUN apt-get update && apt-get install -y nginx

# Define build arguments for AWS credentials and debug mode
ARG AWS_STORAGE_BUCKET_NAME
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG DEBUG

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies specified in the requirements.txt file
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Gunicorn to serve the Django application in a production environment
RUN pip install gunicorn

# Copy the rest of the application code into the container
COPY . .

# Copy the Nginx configuration file into the container
COPY nginx.conf /etc/nginx/sites-available/default

# Remove the default symbolic link for Nginx sites, then create a new one to activate our custom Nginx configuration
RUN rm /etc/nginx/sites-enabled/default && ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Set the Django settings module environment variable for the production environment
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Set environment variables for AWS S3 bucket configuration
ENV AWS_STORAGE_BUCKET_NAME=$AWS_STORAGE_BUCKET_NAME
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV DEBUG=$DEBUG

# Collect static files to be served by S3 Buckets
RUN python manage.py collectstatic --noinput

# Expose ports 80 and 8000 for Nginx and Gunicorn
EXPOSE 80 8000

# Start Nginx and Gunicorn to serve the Django application
CMD service nginx start && gunicorn --bind 0.0.0.0:8000 oc_lettings_site.wsgi:application

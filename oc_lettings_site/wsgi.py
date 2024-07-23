import os

from django.core.wsgi import get_wsgi_application

"""
WSGI configuration for the oc_lettings_site project.

This module contains the WSGI application used for serving the project.
It exposes the WSGI callable as a module-level variable named `application`.

Attributes:
    application (WSGIHandler): The WSGI application callable.
"""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

application = get_wsgi_application()

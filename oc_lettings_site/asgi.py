import os

from django.core.asgi import get_asgi_application

"""
ASGI configuration for the oc_lettings_site project.

This module contains the ASGI application used for serving the project.
It exposes the ASGI callable as a module-level variable named `application`.

Attributes:
    application (ASGIHandler): The ASGI application callable.
"""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

application = get_asgi_application()

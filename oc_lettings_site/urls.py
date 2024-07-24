from django.contrib import admin
from django.urls import path, include
from . import views

"""
URL configuration for the main project.

This module defines the URL patterns for the main project, including paths for
the admin interface, the homepage, and the lettings and profiles apps.

Attributes:
    urlpatterns (list): The list of URL patterns for the main project.

URL Patterns:
    - path("admin/", admin.site.urls):
      Maps the URL `admin/` to the Django admin interface.
    - path("", views.index, name="index"):
      This view displays the homepage.
    - path("lettings/", include("lettings.urls", namespace="lettings")):
      Includes the URL patterns defined in the lettings app. The `namespace`
      argument is used to differentiate namespaced URLs in different apps.
    - path("profiles/", include("profiles.urls", namespace="profiles")):
      Includes the URL patterns defined in the profiles app. The `namespace`
      argument is used to differentiate namespaced URLs in different apps.
"""

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
]

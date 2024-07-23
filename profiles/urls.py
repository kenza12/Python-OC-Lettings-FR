from django.urls import path
from . import views

"""
URL configuration for the profiles app.

This module defines the URL patterns for the profiles app. It includes paths
for listing all profiles and for displaying details of a specific profile.

Attributes:
    app_name (str): The namespace for the app.
    urlpatterns (list): The list of URL patterns for the profiles app.

URL Patterns:
    - path("", views.index, name="index"):
      This view displays the list of all profiles.
    - path("<str:username>/", views.profile, name="profile"):
      This view displays the details of a specific profile identified by the
      `username`.
"""

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>/", views.profile, name="profile"),
]

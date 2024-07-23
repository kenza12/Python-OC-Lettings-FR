from django.urls import path
from . import views

"""
This module defines the URL patterns for the lettings app. It includes paths
for listing all lettings and for displaying details of a specific letting.

Attributes:
    app_name (str): The namespace for the app.
    urlpatterns (list): The list of URL patterns for the lettings app.

URL Patterns:
    - path("", views.index, name="index"):
      This view displays the list of all lettings.

    - path("<int:letting_id>/", views.letting, name="letting"):
      This view displays the details of a specific letting identified by the
      `letting_id`.
"""

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]

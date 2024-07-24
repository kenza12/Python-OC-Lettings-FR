from django.shortcuts import render
from .models import Profile


def index(request):
    """
    This view retrieves all profiles from the database and renders the
    'profiles/index.html' template with the list of profiles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered 'index.html' template with the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    This view retrieves a profile by the associated user's username and renders the
    'profiles/profile.html' template with the profile details.

    Args:
        request (HttpRequest): The request object.
        username (str): The username of the associated user.

    Returns:
        HttpResponse: The rendered 'profile.html' template with the profile details.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)

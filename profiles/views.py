from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Profile
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    This view retrieves all profiles from the database and renders the
    'profiles/index.html' template with the list of profiles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered 'index.html' template with the list of profiles.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)
    except Exception as e:
        logger.error(f"Error retrieving profiles: {e}")
        return HttpResponse("An error occurred while retrieving profiles.")


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
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except Exception as e:
        logger.error(f"Error fetching profile with username {username}: {e}")
        return HttpResponse(f"An error occurred while retrieving the profile for {username}.")

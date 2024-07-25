from django.shortcuts import render, get_object_or_404
from .models import Letting
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    This view retrieves all lettings from the database and renders the
    'lettings/index.html' template with the list of lettings.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered 'index.html' template with the list of lettings.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {"lettings_list": lettings_list}
        return render(request, "lettings/index.html", context)
    except Exception as e:
        logger.error(f"Error retrieving lettings: {e}")
        raise


def letting(request, letting_id):
    """
    This view retrieves a letting by its ID and renders the 'lettings/letting.html'
    template with the letting details.

    Args:
        request (HttpRequest): The request object.
        letting_id (int): The ID of the letting.

    Returns:
        HttpResponse: The rendered 'lettings/letting.html' template with the letting details.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Exception as e:
        logger.error(f"Error fetching letting with id {letting_id}: {e}")
        raise

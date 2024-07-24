from django.shortcuts import render
from .models import Letting


def index(request):
    """
    This view retrieves all lettings from the database and renders the
    'lettings/index.html' template with the list of lettings.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered 'index.html' template with the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


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
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)

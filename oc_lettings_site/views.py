from django.shortcuts import render


def index(request):
    """
    Display the homepage.

    This view renders the 'index.html' template for the homepage.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered 'index.html' template.
    """
    return render(request, "index.html")

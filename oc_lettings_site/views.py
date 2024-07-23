from django.shortcuts import render


def index(request):
    """
    Display the homepage.
    """
    return render(request, 'index.html')

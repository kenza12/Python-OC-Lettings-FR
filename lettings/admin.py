from django.contrib import admin
from .models import Letting, Address

"""
Register the Letting and address models with the Django admin site.
"""

admin.site.register(Letting)
admin.site.register(Address)

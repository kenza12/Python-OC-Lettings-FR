from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile with a favorite city.

    Attributes:
        user (User): The associated user.
        favorite_city (str): The user's favorite city.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the profile.

        Returns:
            str: The username of the associated user.
        """
        return self.user.username

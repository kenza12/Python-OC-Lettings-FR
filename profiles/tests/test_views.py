from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile
from django.core.exceptions import ObjectDoesNotExist
from unittest.mock import patch


class ProfileViewTests(TestCase):
    """
    Test suite for the views in the profiles app.
    """

    def setUp(self):
        """
        Set up sample instances for testing the views.

        Creates a User object and a Profile object with specific attributes.
        """
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_index_view(self):
        """
        Test the profiles index view.

        Verifies that the index view returns a 200 status code and contains the username.
        """
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")

    @patch("profiles.views.Profile.objects.all")
    def test_index_view_exception(self, mock_profiles_all):
        """
        Test the profiles index view when an exception is raised.

        Verifies that the view handles the exception and returns the correct error message.
        """
        mock_profiles_all.side_effect = Exception("Test exception")
        response = self.client.get(reverse("profiles:index"))
        self.assertContains(response, "An error occurred while retrieving profiles.")

    def test_profile_view(self):
        """
        Test the profile detail view.

        Verifies that the profile detail view returns a 200 status code and
        contains the favorite city.
        """
        response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test City")

    @patch("profiles.views.get_object_or_404")
    def test_profile_view_exception(self, mock_get_object_or_404):
        """
        Test the profile detail view when an exception is raised.

        Verifies that the view handles the exception and returns the correct error message.
        """
        mock_get_object_or_404.side_effect = ObjectDoesNotExist("Test exception")
        response = self.client.get(reverse("profiles:profile", args=[self.user.username]))
        self.assertContains(
            response, f"An error occurred while retrieving the profile for {self.user.username}."
        )

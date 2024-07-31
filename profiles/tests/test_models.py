from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):
    """
    Test suite for the Profile model.
    """

    def setUp(self):
        """
        Set up a sample Profile instance for testing.

        Creates a User object and a Profile object with specific attributes.
        """
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profile_creation(self):
        """
        Test the creation of a Profile instance.

        Verifies that the Profile object has the correct attributes.
        """
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.favorite_city, "Test City")

    def test_profile_str(self):
        """
        Test the string representation of a Profile instance.

        Verifies that the __str__ method returns the expected string.
        """
        self.assertEqual(str(self.profile), "testuser")

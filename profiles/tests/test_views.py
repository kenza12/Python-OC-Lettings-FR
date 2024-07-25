from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileViewTests(TestCase):
    """
    Test suite for the views in the profiles app.
    """
    def setUp(self):
        """
        Set up sample instances for testing the views.

        Creates a User object and a Profile object with specific attributes.
        """
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Test City')

    def test_index_view(self):
        """
        Test the profiles index view.

        Verifies that the index view returns a 200 status code and contains the username.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")

    def test_profile_view(self):
        """
        Test the profile detail view.

        Verifies that the profile detail view returns a 200 status code and
        contains the favorite city.
        """
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test City")

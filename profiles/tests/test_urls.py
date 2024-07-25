from django.test import TestCase
from django.urls import resolve, reverse
from profiles.views import index, profile


class ProfilesUrlsTest(TestCase):
    """
    Test suite for the URL patterns in the profiles app.
    """
    def test_profiles_index_url_resolves(self):
        """
        Test that the profiles index URL resolves to the correct view.

        Verifies that the URL pattern for the profiles index page resolves to the index view.
        """
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, index)

    def test_profile_detail_url_resolves(self):
        """
        Test that the profile detail URL resolves to the correct view.

        Verifies that the URL pattern for a specific profile resolves to the profile view.
        """
        url = reverse('profiles:profile', args=['testuser'])
        self.assertEqual(resolve(url).func, profile)

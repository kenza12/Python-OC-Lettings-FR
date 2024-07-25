from django.test import TestCase
from django.urls import resolve, reverse
from lettings.views import index, letting


class LettingsUrlsTest(TestCase):
    """
    Test suite for the URL patterns in the lettings app.
    """
    def test_lettings_index_url_resolves(self):
        """
        Test that the lettings index URL resolves to the correct view.

        Verifies that the URL pattern for the lettings index page resolves to
        the index view.
        """
        url = reverse('lettings:index')
        self.assertEqual(resolve(url).func, index)

    def test_letting_detail_url_resolves(self):
        """
        Test that the letting detail URL resolves to the correct view.

        Verifies that the URL pattern for a specific letting resolves to the letting view.
        """
        url = reverse('lettings:letting', args=[1])
        self.assertEqual(resolve(url).func, letting)

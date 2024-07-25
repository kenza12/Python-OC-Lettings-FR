from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    """
    Test suite for the index view of the main application.
    """
    def test_index_view(self):
        """
        Test the main index view.

        Verifies that the index view returns a 200 status code and contains the welcome message.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Holiday Homes")

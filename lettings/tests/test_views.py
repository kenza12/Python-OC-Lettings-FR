from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address
from unittest.mock import patch
from django.core.exceptions import ObjectDoesNotExist


class LettingsViewsTest(TestCase):
    """
    Test suite for the views in the lettings app.
    """
    def setUp(self):
        """
        Set up sample instances for testing the views.

        Creates an Address object and a Letting object with specific attributes.
        """
        self.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="Anytown",
            state="NY",
            zip_code=12345,
            country_iso_code="USA"
        )
        self.letting = Letting.objects.create(
            title="Cozy Cottage",
            address=self.address
        )

    def test_index_view(self):
        """
        Test the lettings index view.

        Verifies that the index view returns a 200 status code and contains
        the letting title.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cozy Cottage")

    @patch('lettings.views.Letting.objects.all')
    def test_index_view_exception(self, mock_lettings_all):
        """
        Test the lettings index view when an exception is raised.

        Verifies that the view handles the exception and returns the correct error message.
        """
        mock_lettings_all.side_effect = Exception("Test exception")
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, "An error occurred while retrieving lettings.")

    def test_letting_detail_view(self):
        """
        Test the letting detail view.

        Verifies that the letting detail view returns a 200 status code and
        contains the letting title.
        """
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cozy Cottage")

    @patch('lettings.views.get_object_or_404')
    def test_letting_detail_view_exception(self, mock_get_object_or_404):
        """
        Test the letting detail view when an exception is raised.

        Verifies that the view handles the exception and returns the correct error message.
        """
        mock_get_object_or_404.side_effect = ObjectDoesNotExist("Test exception")
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertContains(response, "An error occurred while retrieving the letting.")

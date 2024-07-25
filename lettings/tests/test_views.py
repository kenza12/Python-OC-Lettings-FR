from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


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

    def test_letting_detail_view(self):
        """
        Test the letting detail view.

        Verifies that the letting detail view returns a 200 status code and
        contains the letting title.
        """
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cozy Cottage")

from django.test import TestCase
from lettings.models import Address, Letting


class AddressModelTest(TestCase):
    """
    Test suite for the Address model.
    """

    def setUp(self):
        """
        Set up a sample Address instance for testing.

        Creates an Address object with specific attributes.
        """
        self.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="Anytown",
            state="NY",
            zip_code=12345,
            country_iso_code="USA",
        )

    def test_address_creation(self):
        """
        Test the creation of an Address instance.

        Verifies that the Address object has the correct attributes.
        """
        self.assertEqual(self.address.number, 123)
        self.assertEqual(self.address.street, "Main Street")
        self.assertEqual(self.address.city, "Anytown")
        self.assertEqual(self.address.state, "NY")
        self.assertEqual(self.address.zip_code, 12345)
        self.assertEqual(self.address.country_iso_code, "USA")

    def test_address_str(self):
        """
        Test the string representation of an Address instance.

        Verifies that the __str__ method returns the expected string.
        """
        self.assertEqual(str(self.address), "123 Main Street")


class LettingModelTest(TestCase):
    """
    Test suite for the Letting model.
    """

    def setUp(self):
        """
        Set up a sample Letting instance for testing.

        Creates an Address object and a Letting object with specific attributes.
        """
        self.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="Anytown",
            state="NY",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(title="Cozy Cottage", address=self.address)

    def test_letting_creation(self):
        """
        Test the creation of a Letting instance.

        Verifies that the Letting object has the correct attributes.
        """
        self.assertEqual(self.letting.title, "Cozy Cottage")
        self.assertEqual(self.letting.address, self.address)

    def test_letting_str(self):
        """
        Test the string representation of a Letting instance.

        Verifies that the __str__ method returns the expected string.
        """
        self.assertEqual(str(self.letting), "Cozy Cottage")

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an address with number, street, city, state, zip code, and country ISO code.

    Attributes:
        number (int): The house number.
        street (str): The street name.
        city (str): The city name.
        state (str): The state code (2 characters).
        zip_code (int): The zip code.
        country_iso_code (str): The country ISO code (3 characters).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns a string representation of the address.

        Returns:
            str: The formatted address.
        """
        return f"{self.number} {self.street}"

    class Meta:
        """
        Meta options for the Address model.

        Attributes:
            verbose_name_plural (str): The plural name for the Address model.
        """

        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represents a letting associated with an address.

    Attributes:
        title (str): The title of the letting.
        address (Address): The associated address.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the letting.

        Returns:
            str: The title of the letting.
        """
        return self.title

from django.db import models


class Product(models.Model):
    """
    Model representing a product with details like name, light requirement,
    ease of care, pet safety, image, and description.
    """
    LIGHT_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('bright', 'Bright'),
    ]

    EASE_OF_CARE_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('difficult', 'Difficult'),
    ]

    easy_name = models.CharField(max_length=200)
    scientific_name = models.CharField(
        max_length=200, null=True, blank=True
    )
    light = models.CharField(
        max_length=6, choices=LIGHT_CHOICES, default='medium'
    )
    ease_of_care = models.CharField(
        max_length=9, choices=EASE_OF_CARE_CHOICES, default='moderate'
    )
    pet_ok = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='', default='no-image-available.png'
    )
    description = models.TextField(default='No description available')

    def __str__(self):
        return self.easy_name

    @property
    def smallest_price(self):
        prices = self.prices.all()
        if prices:
            return min(price.price for price in prices)
        return None


class PlantSize(models.Model):
    """
    Model representing the size of a plant with a reference to the product,
    size label, and height.
    """
    SIZE_CHOICES = [
        ('sm', 'Small'),
        ('med', 'Medium'),
        ('lg', 'Large'),
    ]

    plant = models.ForeignKey(
        Product, related_name='sizes', on_delete=models.CASCADE
    )
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    height = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.plant.easy_name} - {self.get_size_display()}"


class PlantPrice(models.Model):
    """
    Model representing the price of a plant size with a
    reference to the product, size label, and price.
    """
    SIZE_CHOICES = [
        ('sm', 'Small'),
        ('med', 'Medium'),
        ('lg', 'Large'),
    ]

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='prices'
    )
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return (
            f"{self.product.easy_name} - {self.get_size_display()} - "
            f"{self.price}"
        )

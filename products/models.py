from django.db import models

class Product(models.Model):
    LIGHT_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'Bright'),
    ]

    HEIGHT_CHOICES = [
        ('short', 'Short'),
        ('medium', 'Medium'),
        ('tall', 'Tall'),
    ]

    EASE_OF_CARE_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('difficult', 'Difficult'),
    ]
    easy_name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200, null=True, blank=True)
    light = models.CharField(max_length=6, choices=LIGHT_CHOICES, default='medium')
    height = models.CharField(max_length=6, choices=HEIGHT_CHOICES, default='medium')
    ease_of_care = models.CharField(max_length=9, choices=EASE_OF_CARE_CHOICES, default='moderate')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='plant-images/', default='default_images/no-image-available.png')
    description = models.TextField(default='')

    def __str__(self):
        return self.easy_name

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False) 
        super().delete(*args, **kwargs)
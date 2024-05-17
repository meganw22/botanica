from django.db import models

class Product(models.Model):
    easy_name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200, null=True, blank=True)
    height = models.CharField(max_length=200)
    care_level = models.CharField(max_length=200)
    light_level = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='plant-images/', default='default_images/no-image-available.png')
    description = models.TextField(default='')

    def __str__(self):
        return self.easy_name

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False) 
        super().delete(*args, **kwargs)
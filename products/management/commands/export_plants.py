import json
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    """
    Export all plant data to a JSON file.
    """

    def handle(self, *args, **kwargs):
        products = Product.objects.all().values(
            'easy_name',
            'scientific_name',
            'light',
            'height',
            'ease_of_care',
            'image',
            'description'
        )
        products_list = list(products)
        with open('plants.json', 'w') as json_file:
            json.dump(products_list, json_file, indent=4)

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully exported plant data to plants.json'
                )
            )
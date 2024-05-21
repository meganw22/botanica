import json
from django.core.management.base import BaseCommand
from products.models import Product, PlantSize

class Command(BaseCommand):
    help = 'Load product data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the JSON file.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                product_data = item['fields']
                product, created = Product.objects.update_or_create(
                    pk=item['pk'],
                    defaults={
                        'easy_name': product_data['easy_name'],
                        'scientific_name': product_data.get('scientific_name', ''),
                        'light': product_data['light'],
                        'ease_of_care': product_data['ease_of_care'],
                        'price': product_data.get('price', 0),
                        'image': product_data.get('image', 'default_images/no-image-available.png'),
                        'description': product_data['description'],
                    }
                )
                # Clear existing sizes
                PlantSize.objects.filter(plant=product).delete()

                # Add new sizes
                PlantSize.objects.create(plant=product, size='sm', height=product_data['height-sm'])
                PlantSize.objects.create(plant=product, size='med', height=product_data['height-med'])
                PlantSize.objects.create(plant=product, size='lg', height=product_data['height-lg'])

        self.stdout.write(self.style.SUCCESS('Successfully loaded product data'))

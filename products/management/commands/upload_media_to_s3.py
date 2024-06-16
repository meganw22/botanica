# yourapp/management/commands/upload_media_to_s3.py
from django.core.management.base import BaseCommand
import os
from django.conf import settings
from django.core.files.storage import default_storage

class Command(BaseCommand):
    help = 'Upload local media files to S3'

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT

        for root, dirs, files in os.walk(media_root):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    default_storage.save(file_path.replace(media_root + '/', ''), f)
        self.stdout.write(self.style.SUCCESS('Successfully uploaded media files to S3'))

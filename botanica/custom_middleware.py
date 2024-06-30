# custom_middleware.py
from django.utils.deprecation import MiddlewareMixin

class RemoveXFrameOptionsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if 'X-Frame-Options' in response:
            del response['X-Frame-Options']
        return response

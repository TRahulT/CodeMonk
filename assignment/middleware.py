from datetime import datetime
import jwt
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse


class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == reverse('customuser-login'):
            return self.get_response(request)
        if request.path.startswith('/admin/'):
            # Allow superusers to access the admin site
                return self.get_response(request)

        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]
        if token:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                request.user_id = payload['user_id']

            except jwt.ExpiredSignatureError:
                return JsonResponse({'error': 'Token expired',"is_vaild":False}, status=401)
            except jwt.DecodeError:
                return JsonResponse({'error': 'Token invalid',"is_vaild":False}, status=401)
        else:
            return JsonResponse({"default":"no Token","is_vaild":False})
        return self.get_response(request)

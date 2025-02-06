from django.contrib.auth.backends import BaseBackend
from api.models import User


class PasswordLessAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # if username == 'superuser':
            #     return None
            # return User.objects.get(username=username)
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

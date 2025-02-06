import os
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'AFP.settings')

import django

django.setup()

from api.models import User, Role, Permission


def populate():
    permissions = Permission.objects.all()

    try:
        role = Role.objects.get(code_name='su')
        role.permissions.clear()
    except Role.DoesNotExist:
        role = Role.objects.create(name='SuperUser', code_name='su')

    role.permissions.add(*permissions)
    role.save()

    try:
        user = User.objects.get(username='superuser')
    except User.DoesNotExist:
        user = User.objects.create_superuser(
            cnic = '1234567890001',
            mobile = '03257896541',
            username="superuser",
            password="123",
            is_staff = True
        )
        user.name = 'Superuser'
        user.role = Role.objects.get(code_name='su')
        user.save()


if __name__ == '__main__':
    print("Starting AFP population script...")
    populate()

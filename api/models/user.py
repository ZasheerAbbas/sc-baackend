from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator
import uuid


def get_profile_image_path(self, filename):
    return f'profile_images/users/{self.pk}/{str(uuid.uuid4())}.png'


def get_default_profile_image_path():
    return f'profile_images/{"default_profile_image.png"}'


class UserManager(BaseUserManager):
    def create_user(self, cnic , mobile, username = None, password=None , first_name = None, last_name = None,is_staff = False):
        if not cnic:
            raise ValueError('User must have a cnic.')
        if not mobile:
            raise ValueError('User must have a mobile.')
        user = self.model(
            username = username,
            cnic=cnic,
            mobile=mobile,
            is_staff = is_staff,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cnic, mobile,  username = None,password = None,is_staff = False ):
        user = self.create_user(
            cnic=cnic,
            mobile=mobile,
            username = username,
            password=password,
            is_staff = is_staff
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    cnic = models.IntegerField(max_length=50, null=True)
    mobile = models.CharField(max_length=15)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=60,  unique=True)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_path, null=True, blank=True,
                                      default=get_default_profile_image_path)
    
    is_staff                = models.BooleanField(default=False)
    role = models.ForeignKey('Role', related_name='users', blank=True, null=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

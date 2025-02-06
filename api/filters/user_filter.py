import django_filters as filters
from api.models import User


class UserFilter(filters.FilterSet):
    organization = filters.NumberFilter(field_name='organization__id')

    class Meta:
        model = User
        fields = ['organization']

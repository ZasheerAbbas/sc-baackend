from rest_framework import serializers
from api.models import User, Role


class UserSerializer(serializers.ModelSerializer):

    role_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_role_data(self, obj):
        if not obj.role:
            return None

        role = Role.objects.get(pk=obj.role.id)
        data = {
            'name': role.name,
            'code_name': role.code_name
        }
        return data
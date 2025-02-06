from rest_framework import serializers
from api.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    file_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Document
        fields = (
            'id', 'path', 'file_data'
        )
        read_only_fields = ('file_data', )

    def get_file_data(self, obj):
        if not obj.path:
            return None

        data = {
            'name': obj.path.name.split('/')[-1],
        }
        return data

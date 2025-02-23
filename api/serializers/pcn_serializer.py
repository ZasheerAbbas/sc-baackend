# serializers.py
from rest_framework import serializers
from api.models import Product, Container, Notification

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'

    def update(self, instance, validated_data):
        new_level = validated_data.get('current_level', instance.current_level)
        
        # Check if level drops below threshold
        if new_level < instance.threshold and instance.current_level >= instance.threshold:
            Notification.objects.create(
                user=instance.user,
                container=instance,
                message=f"{instance.product.name} level dropped below {instance.threshold}%"
            )
        
        return super().update(instance, validated_data)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
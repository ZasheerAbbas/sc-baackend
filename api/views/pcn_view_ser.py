# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import Product, Container, Notification
from api.serializers import ProductSerializer, ContainerSerializer, NotificationSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ContainerViewSet(viewsets.ModelViewSet):
    serializer_class = ContainerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Container.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'patch', 'head', 'options']

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
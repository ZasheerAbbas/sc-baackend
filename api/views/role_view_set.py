from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import Role, Logs
from api.serializers import RoleSerializer
from api.decorator import route_permissions
from api.paginations import CustomPagination


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.exclude(code_name='su').order_by('id')
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = CustomPagination

    @route_permissions(['role_read'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @route_permissions(['role_create'])
    def create(self, request, *args, **kwargs):
        Logs.objects.create(text='Role created', created_by=request.user)
        return super().create(request, *args, **kwargs)

    @route_permissions(['role_read'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @route_permissions(['role_update'])
    def update(self, request, *args, **kwargs):
        Logs.objects.create(text='Role updated', created_by=request.user)
        return super().update(request, *args, **kwargs)

    @route_permissions(['role_update'])
    def partial_update(self, request, *args, **kwargs):
        Logs.objects.create(text='Role updated', created_by=request.user)
        return super().partial_update(request, *args, **kwargs)

    @route_permissions(['role_delete'])
    def destroy(self, request, *args, **kwargs):
        Logs.objects.create(text='Role deleted', created_by=request.user)
        return super().destroy(request, *args, **kwargs)

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UserSerializer
from api.util import combine_role_permissions


class CurrentUserView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        try:
            data = UserSerializer(request.user, context={'request': request}).data
            data['permissions'] = combine_role_permissions(request.user.role)
            return Response({"user": data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"user": None}, status=status.HTTP_400_BAD_REQUEST)


from api.serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from api.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class UserChangePasswordView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                old = serializer.validated_data.get('old_password')
                new = serializer.validated_data.get('new_password')
                try:
                    user = User.objects.get(pk = request.user.pk)
                except User.DoesNotExist:
                    raise Http404
                if user.check_password(old):
                    user.set_password(new)
                    user.updated_by = request.user
                    user.save()
                    return Response({'msg': 'Password Successfully Changed'}, status=status.HTTP_200_OK)
                else:
                    return Response({'msg': 'Incorrect Password'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'msg' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg': f'ERROR : {e}'}, status=status.HTTP_400_BAD_REQUEST)
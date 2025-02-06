from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import User
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from api.serializers import UserSerializer
class ProfileUpdateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        try:
            user_obj = self.get_object(pk)
            data = request.data
            data['updated_by'] = request.user
            serializer = UserSerializer(user_obj, data = data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg' : 'Successfully Updated User Data', 'data' : serializer.data}, status=status.HTTP_200_OK)
            else:
                print("ÏNVALID : " , serializer.errors)
            return Response({'msg' : 'Failed to Update User Data'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg' : f'Error in Update : {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

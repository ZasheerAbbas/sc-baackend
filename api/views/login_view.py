from django.middleware import csrf
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.util import set_access_cookies, set_refresh_cookies, get_tokens_for_user, combine_role_permissions
from api.serializers import UserSerializer


class LoginView(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny, )

    def post(self, request):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        if not username or not password:
            return Response({"msg": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is not None:

            response = Response()

            token = get_tokens_for_user(user)
            set_access_cookies(response, token['access'])
            set_refresh_cookies(response, token['refresh'])
            csrf.get_token(request)

            data = UserSerializer(user, context={'request': request}).data
            data['permissions'] = combine_role_permissions(user.role)

            response.status_code = status.HTTP_200_OK
            response.data = {"msg": "Login successfully", "user": data}
            return response
        else:
            return Response({"msg": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)

from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, api_settings as jwt_settings
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentication import JWTCookieAuthentication
from .permissions import IsAuthenticatedOrPost
from .serializers import UserSerializer


@csrf_exempt
class UserView(APIView):
    permission_classes = (IsAuthenticatedOrPost, )
    authentication_classes = JWTAuthentication, JWTCookieAuthentication

    def get(self, request: Request):
        user_id = request.user.id
        user_instance = get_user_model().objects.get(pk=user_id)
        serialized_user = UserSerializer(instance=user_instance)
        return Response(serialized_user.data)

    def post(self, request: Request):
        serialized_user = UserSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response(serialized_user.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes((BasicAuthentication, ))
@permission_classes((IsAuthenticated, ))
def create_jwt_token_view(request: Request):
    user_id = request.user.id
    user_instance = get_user_model().objects.get(pk=user_id)
    jwt_token = RefreshToken.for_user(user_instance)
    access_token, refresh_token = jwt_token.access_token, jwt_token
    response_data = {'access': str(access_token), 'refresh': str(refresh_token)}
    return Response(response_data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes((BasicAuthentication, ))
@permission_classes((IsAuthenticated, ))
def create_cookie_authentication_view(request: Request):
    user_id = request.user.id
    user_instance = get_user_model().objects.get(pk=user_id)
    jwt_token = AccessToken.for_user(user_instance)
    cookie_key = api_settings.user_settings['JWT_TOKEN_KEY']
    response = Response(status=status.HTTP_201_CREATED)
    response.set_cookie(cookie_key,
                        str(jwt_token),
                        jwt_settings.ACCESS_TOKEN_LIFETIME.seconds,
                        httponly=True)
    return response


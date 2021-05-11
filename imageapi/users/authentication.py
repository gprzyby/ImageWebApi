from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from rest_framework.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken


class JWTCookieAuthentication(JWTAuthentication):
    cookie_key = api_settings.user_settings['JWT_TOKEN_KEY']

    def authenticate(self, request: Request):
        token = request.COOKIES.get(self.cookie_key, None)

        if not token:
            return None

        validated_token = self.get_validated_token(token)

        return self.get_user(validated_token), validated_token

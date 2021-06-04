from django.urls import path
from .views import UserView, create_jwt_token_view, create_cookie_authentication_view

urlpatterns = [
    path('', UserView().as_view(), name='user_view'),
    path('token', create_jwt_token_view, name='user_token_creation'),
    path('cookie', create_cookie_authentication_view, name='user_cookie_creation'),
]
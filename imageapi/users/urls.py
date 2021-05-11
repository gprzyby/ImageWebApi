from django.urls import path
from .views import UserView, create_jwt_token_view, create_cookie_authentication_view

urlpatterns = [
    path('', UserView().as_view()),
    path('token', create_jwt_token_view),
    path('cookie', create_cookie_authentication_view),
]
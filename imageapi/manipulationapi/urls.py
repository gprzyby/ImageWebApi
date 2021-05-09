from django.urls import path
from .views import get_image_info

urlpatterns = [
    path('', get_image_info)
]
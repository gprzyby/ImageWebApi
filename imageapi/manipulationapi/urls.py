from django.urls import path
from .views import get_image_info, ImageCreationView, GetUpdateRemoveImageView

urlpatterns = [
    path('', ImageCreationView.as_view()),
    path('<int:id>', GetUpdateRemoveImageView.as_view())
]
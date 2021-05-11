from django.urls import path
from .views import get_image_file_view, ImageCreationView, GetUpdateRemoveImageView, crop_image_view, scale_image_view

urlpatterns = [
    path('', ImageCreationView.as_view()),
    path('<int:id>', GetUpdateRemoveImageView.as_view()),
    path('<int:id>/image', get_image_file_view),
    path('<int:id>/image/crop/<int:start_x>/<int:start_y>/<int:end_x>/<int:end_y>', crop_image_view),
    path('<int:id>/image/scale', scale_image_view),
]
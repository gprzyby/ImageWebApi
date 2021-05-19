from django.urls import path
from .views import ImageCreationView, GetUpdateRemoveImageView, GetImageFileView, CropImageView, ScaleImageView

urlpatterns = [
    path('', ImageCreationView.as_view()),
    path('<int:id>', GetUpdateRemoveImageView.as_view()),
    path('<int:id>/image', GetImageFileView.as_view()),
    path('<int:id>/image/crop/<int:start_x>/<int:start_y>/<int:end_x>/<int:end_y>', CropImageView.as_view()),
    path('<int:id>/image/scale', ScaleImageView.as_view()),
]
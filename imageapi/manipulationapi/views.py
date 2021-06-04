from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from guardian.shortcuts import assign_perm

from manipulationapi import services
from manipulationapi.models import ImageStorage
from manipulationapi.serializers import ImageStorageSerializer
from manipulationapi.utils import convert_to_image_file

from users.authentication import JWTCookieAuthentication
from users.permissions import IsModelOwner
from imageapi.renderers import PngRenderer


class ImageCreationView(generics.ListCreateAPIView):
    serializer_class = ImageStorageSerializer
    authentication_classes = JWTCookieAuthentication, JWTAuthentication
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user_id = self.request.user.id

        return ImageStorage.objects.filter(owner__id=user_id)

    def perform_create(self, serializer: ImageStorageSerializer):
        authenticated_user = self.request.user
        created_object = serializer.save(owner=authenticated_user)
        self.assign_permissions(created_object, authenticated_user.pk)

    def assign_permissions(self, created_object, creator_id):
        creator = get_user_model().objects.get(id=creator_id)
        permissions_to_assign = [f'manipulationapi.{method}_imagestorage'
                                 for method in ['add', 'change', 'delete', 'view']]

        for permission in permissions_to_assign:
            assign_perm(permission, creator, created_object)


class GetUpdateRemoveImageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageStorageSerializer
    lookup_field = 'id'
    queryset = ImageStorage.objects
    permission_classes = IsAuthenticated, IsModelOwner
    authentication_classes = JWTCookieAuthentication, JWTAuthentication


class BaseImageFileView(generics.GenericAPIView):
    permission_classes = IsAuthenticated, IsModelOwner
    renderer_classes = (PngRenderer, )
    queryset = ImageStorage.objects
    lookup_field = 'id'

    def get_image_file(self):
        image_storage = self.get_object()
        return convert_to_image_file(image_storage)


class GetImageFileView(BaseImageFileView):

    def get(self, request: Request, **kwargs):
        return Response(self.get_image_file())


class CropImageView(BaseImageFileView):

    def get(self, start_x: int, start_y: int, end_x: int, end_y: int, **kwargs):
        image_file = self.get_image_file()
        cropped_image = services.crop_image(image_file, start_x, start_y, end_x, end_y)
        return Response(data=cropped_image)


class ScaleImageView(BaseImageFileView):

    def get(self, request: Request, **kwargs):
        scale = float(request.query_params.get('scale', '1'))
        image_file = self.get_image_file()
        scaled_image = services.scale_image(image_file, scale)
        return Response(data=scaled_image)


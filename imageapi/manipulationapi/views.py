from django.contrib.auth import get_user_model
from rest_framework import views, generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
import rest_framework.status as http_status
from rest_framework_simplejwt.authentication import JWTAuthentication
from guardian.shortcuts import assign_perm

from imageapi.renderers import PngRenderer
from manipulationapi import services
from manipulationapi.models import ImageStorage
from manipulationapi.serializers import ImageStorageSerializer
from manipulationapi.utils import get_image_file_by_id
from users.authentication import JWTCookieAuthentication
from users.permissions import IsModelOwner


class ImageCreationView(generics.ListCreateAPIView):
    serializer_class = ImageStorageSerializer
    authentication_classes = JWTCookieAuthentication, JWTAuthentication
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        user_id = self.request.user.id

        return ImageStorage.objects.filter(owner__id=user_id)

    def perform_create(self, serializer: ImageStorageSerializer):
        authenticated_user = self.request.user
        created_object = serializer.save(owner=authenticated_user)
        self.assign_permissions(created_object, authenticated_user.pk)

    def assign_permissions(self, created_object, creator_id):
        creator = get_user_model().objects.get(id=creator_id)
        permissions_to_assign = [f'manipulationapi.{method}_imagestorage' for method in ['add', 'change', 'delete', 'view']]

        for permission in permissions_to_assign:
            assign_perm(permission, creator, created_object)



class GetUpdateRemoveImageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageStorageSerializer
    lookup_field = 'id'
    queryset = ImageStorage.objects
    permission_classes = IsAuthenticated
    authentication_classes = JWTCookieAuthentication, JWTAuthentication


@api_view(['GET'])
@renderer_classes([PngRenderer])
def get_image_file_view(request: Request, id: int):
    image_file = get_image_file_by_id(id)
    return Response(data=image_file)


@api_view(['GET'])
@renderer_classes([PngRenderer, JSONRenderer])
def crop_image_view(request: Request, id: int, start_x: int, start_y: int, end_x: int, end_y: int):
    image_file = get_image_file_by_id(id)
    cropped_image = services.crop_image(image_file, start_x, start_y, end_x, end_y)
    return Response(data=cropped_image)


@api_view(['GET'])
@renderer_classes([PngRenderer])
def scale_image_view(request: Request, id: int):
    scale = float(request.query_params.get('scale'))
    image_file = get_image_file_by_id(id)
    scaled_image = services.scale_image(image_file, scale)
    return Response(data=scaled_image)

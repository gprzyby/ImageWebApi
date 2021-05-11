from rest_framework import views, generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.request import Request
from rest_framework.response import Response
import rest_framework.status as http_status

from imageapi.renderers import PngRenderer
from manipulationapi import services
from manipulationapi.models import ImageStorage
from manipulationapi.serializers import ImageStorageSerializer
from manipulationapi.utils import get_image_file_by_id


class ImageCreationView(generics.CreateAPIView):
    serializer_class = ImageStorageSerializer


class GetUpdateRemoveImageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageStorageSerializer
    lookup_field = 'id'
    queryset = ImageStorage.objects


@api_view(['GET'])
@renderer_classes([PngRenderer])
def get_image_file_view(request: Request, id: int):
    image_file = get_image_file_by_id(id)
    return Response(data=image_file)


@api_view(['GET'])
@renderer_classes([PngRenderer])
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

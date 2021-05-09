import PIL.Image as Images
from io import BytesIO

from PIL.PngImagePlugin import PngImageFile
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views, generics
from rest_framework.decorators import api_view, parser_classes, renderer_classes
from rest_framework.generics import get_object_or_404
from rest_framework.negotiation import BaseContentNegotiation
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.request import Request
from rest_framework.response import Response
import rest_framework.status as http_status

from imageapi.parsers import PngImageParser
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
def get_image_file(request: Request, id: int):
    image_file = get_image_file_by_id(id)
    return Response(data=image_file, status=http_status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([PngRenderer])
def crop_image(request: Request, id: int, start_x: int, start_y: int, end_x: int, end_y: int):
    image_file = get_image_file_by_id(id)
    cropped_image = services.crop_image(image_file, start_x, start_y, end_x, end_y)
    return Response(data=cropped_image, status=http_status.HTTP_200_OK)


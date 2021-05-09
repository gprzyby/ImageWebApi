import PIL.Image as Images
from io import BytesIO

from PIL.PngImagePlugin import PngImageFile
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views, generics
from rest_framework.decorators import api_view, parser_classes, renderer_classes
from rest_framework.request import Request
from rest_framework.response import Response
import rest_framework.status as http_status

from imageapi.parsers import PngImageParser
from imageapi.renderers import PngRenderer
from manipulationapi.models import ImageStorage
from manipulationapi.serializers import ImageStorageSerializer


@csrf_exempt
@api_view(['POST'])
@parser_classes([PngImageParser])
@renderer_classes([PngRenderer])
def get_image_info(request: Request):
    raw_image: PngImageFile = request.data
    return Response(data=raw_image, status=http_status.HTTP_200_OK)


class ImageCreationView(generics.CreateAPIView):
    serializer_class = ImageStorageSerializer


class GetUpdateRemoveImageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageStorageSerializer
    lookup_field = 'id'
    queryset = ImageStorage.objects


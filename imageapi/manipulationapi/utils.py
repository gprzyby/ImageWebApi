from PIL.ImageFile import ImageFile
from PIL.Image import open as open_as_image
from django.shortcuts import get_object_or_404

from manipulationapi.models import ImageStorage


def get_image_file_by_id(image_storage_id: int) -> ImageFile:
    image = get_object_or_404(ImageStorage.objects, pk=image_storage_id)
    return convert_to_image_file(image)


def convert_to_image_file(image_storage: ImageStorage) -> ImageFile:
    image_path = image_storage.image_url.path
    return open_as_image(image_path)
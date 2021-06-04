from PIL.ImageFile import Image
from rest_framework.exceptions import ValidationError


def validate_crop_image_data(image: Image, start_x: int, start_y: int, end_x: int, end_y: int):
    if not (0 <= start_x < end_x <= image.width and 0 <= start_y < end_y <= image.height):
        raise ValidationError('Wrong coordinates')


def crop_image(image: Image, start_x: int, start_y: int, end_x: int, end_y: int) -> Image:
    validate_crop_image_data(image, start_x, start_y, end_x, end_y)
    return image.crop(box=(start_x, start_y, end_x, end_y))


def validate_scale_data(image, scale):
    if not scale or scale <= 0 or not image:
        raise ValidationError('Wrong scale of image cannot be less or equal zero')


def scale_image(image: Image, scale: float) -> Image:
    validate_scale_data(image, scale)
    destination_size = (int(image.width * scale), int(image.height * scale))
    return image.resize(destination_size)
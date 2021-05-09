from PIL.ImageFile import ImageFile
from rest_framework.exceptions import ParseError


def validate_crop_image_data(image_file: ImageFile, start_x: int, start_y: int, end_x: int, end_y: int):
    if not (0 < start_x < end_x < image_file.width and 0 < start_y < end_y < image_file.height):
        raise ParseError('Wrong coordinates')


def crop_image(image_file: ImageFile, start_x: int, start_y: int, end_x: int, end_y: int) -> ImageFile:
    validate_crop_image_data(image_file, start_x, start_y, end_x, end_y)
    return image_file.crop(box=(start_x, start_y, end_x, end_y))

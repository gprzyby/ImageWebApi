from rest_framework.parsers import BaseParser
from PIL.Image import open as open_image


class PngImageParser(BaseParser):
    """
    Png image parser
    """
    media_type = 'image/png'

    def parse(self, stream, media_type=None, parser_context=None):
        decoded_image = open_image(stream)
        return decoded_image


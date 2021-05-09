from io import BytesIO

from PIL import Image
from rest_framework.renderers import BaseRenderer


class PngRenderer(BaseRenderer):
    media_type = 'image/png'
    format = 'png'
    charset = None
    render_style = 'binary'

    def render(self, data: Image.Image, accepted_media_type=None, renderer_context=None):
        if not isinstance(data, Image.Image):
            return data

        return self._save_image_into_buffer(data)

    def _save_image_into_buffer(self, image: Image.Image):
        buffer = BytesIO()
        image.save(buffer, format='png')
        return buffer.getbuffer()

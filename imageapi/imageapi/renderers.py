from io import BytesIO

from rest_framework.renderers import BaseRenderer


class PngRenderer(BaseRenderer):
    media_type = 'image/png'
    format = 'png'
    charset = None
    render_style = 'binary'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        buffer = BytesIO()
        data.save(buffer, format='png')
        return buffer.getbuffer()


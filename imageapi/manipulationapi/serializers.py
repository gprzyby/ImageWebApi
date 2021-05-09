from rest_framework.serializers import ModelSerializer

from manipulationapi.models import ImageStorage


class ImageStorageSerializer(ModelSerializer):
    class Meta:
        model = ImageStorage
        fields = '__all__'
        read_only_fields = ['id']
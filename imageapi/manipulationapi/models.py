from django.db import models
from django.conf import settings


# Create your models here.
class ImageStorage(models.Model):
    image_title = models.CharField(max_length=255, null=False, blank=False, default='unnamed')
    image_url = models.ImageField(upload_to='images')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
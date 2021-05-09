from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
class ImageStorage(models.Model):
    image_title = models.CharField(max_length=255, null=False, blank=False, default='unnamed')
    image_url = models.ImageField(upload_to='images')
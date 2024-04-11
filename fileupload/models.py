from django.db import models

# Create your models here.
class FilesUpload(models.Model):
    file = models.FileField()

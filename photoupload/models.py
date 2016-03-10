from django.db import models

# Create your models here.
class Picture(models.Model):
    picfile = models.FileField(upload_to='pictures')
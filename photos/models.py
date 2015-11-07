from django.db import models

# Create your models here.

class Photo(models.Model):
    """
    Model to represent a image model,
    """
    name = models.CharField(max_length=50,
                            blank=True)
    title = models.CharField(max_length=50,
                             blank=True)
    photo_document = models.FileField(upload_to="normal/photos/%y/%m/%d/",
                                      null=True,
                                      blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
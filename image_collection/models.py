from django.db import models
from djongo import models as djongo_models

class Image_collection(models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    key_points = models.JSONField(default=list)
    imageBase64 = models.TextField()
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

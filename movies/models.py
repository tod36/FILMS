from django.db import models
import uuid


class Film(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    length = models.CharField(max_length=120)
    year = models.DateField(auto_now_add=True)
    genre = models.TextField()

    def __str__(self):
        return self.title

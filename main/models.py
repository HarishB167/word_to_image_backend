from django.db import models

class ImageWord(models.Model):
    label = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self) -> str:
        return self.label


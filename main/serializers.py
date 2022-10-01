from rest_framework import serializers
from . import models


class ImageWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageWord
        fields = ["label", "url"]

from rest_framework import serializers
from .models import Image

#Seralizer de las imagenes
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
from rest_framework import routers, serializers, viewsets

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ['name', 'title', 'photo_document',
                  'description']


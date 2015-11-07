from django.shortcuts import render

from rest_framework.views import APIView
from braces.views import JSONResponseMixin

from .serializers import PhotoSerializer
from .models import Photo

# Create your views here.


class QuestionApiView(JSONResponseMixin, APIView):
    """
    View to add address to logged-in users.
    """

    def get(self, request, format=None):
        """
        Fetch the logged in user's addresses and
        return them.
        """
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return self.render_json_response(serializer.data)

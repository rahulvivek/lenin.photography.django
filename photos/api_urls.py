from django.conf.urls import include, url

from .views import QuestionApiView

urlpatterns = [
    url(r'^photos/$',
        QuestionApiView.as_view(),
        name='photo_api_view'),
]
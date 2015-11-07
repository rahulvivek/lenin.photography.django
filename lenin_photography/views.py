from django.views.generic import (TemplateView)

class OnlineAppView(TemplateView):
    """ View to render a static Template for online app """
    template_name = 'online_app.html'
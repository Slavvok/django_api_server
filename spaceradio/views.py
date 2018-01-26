from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import MessageSerializer
from .models import Message

class MainView(TemplateView):
    template_name = 'spaceradio/index.html'

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    def get_serializer_class(self):
        return MessageSerializer

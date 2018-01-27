from django.views.generic import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import MessageSerializer
from .models import Message

class MainView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'spaceradio/index.html'
    def get(self, request):
        queryset = Message.objects.all()
        return Response({'messages':queryset})

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    def get_serializer_class(self):
        return MessageSerializer

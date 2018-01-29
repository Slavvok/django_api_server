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
    serializer_class = MessageSerializer
    queryset = Message.objects.filter(isread = False)
    @property
    def mark_read(self, request):
        self.read = Message.objects.all().set(isread=True)
        return Response({'read' :self.read})

'''
class MarkRead(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    queryset.isread.set(False)

    def mark_read(self, request):
        self.read = Message.objects.all().set(isread=True)
        return Response({'read' :self.read})
'''

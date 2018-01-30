from django.views.generic import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import detail_route
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
    @detail_route(methods=['get','put'], url_name='mark_read/')
    def mark_read(self, request, pk=None):
        queryset = Message.objects.filter(pk=pk).update(isread=True)
        return Response({'read':queryset})
'''
class MarkReadViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    def mark_read(self, request, pk):
        queryset = Message.objects.update(isread=False)
        return Response({'read':queryset})
'''

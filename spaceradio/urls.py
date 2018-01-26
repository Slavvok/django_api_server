from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'api/get_messages', MessageViewSet)

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^', include(router.urls))
]

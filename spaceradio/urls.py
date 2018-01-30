from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'api/get_messages', MessageViewSet)
#router.register(r'api/mark_read', MarkReadViewSet),

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
    #url(r'', MessageViewSet.as_view({'isread':'mark_read'}), name='read'),
    url(r'^', include(router.urls))
]

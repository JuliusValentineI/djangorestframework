from django.urls import path, include
from rest_framework import routers
from .views import ProgrammerViewSet


router = routers.DefaultRouter()
router.register(r'programmers', ProgrammerViewSet)

urlpatterns = [
    path('', include(router.urls))
]


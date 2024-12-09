from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import readiness_check, liveness_check

from api import views

app_name = "api"
urlpatterns = [
    path('readiness', readiness_check, name='readiness_check'),
    path('liveness', liveness_check, name='liveness_check'),
    path('', include(router.urls)),
]

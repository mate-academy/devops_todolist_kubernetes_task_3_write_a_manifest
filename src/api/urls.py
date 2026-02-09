from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.http import HttpResponse

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

def health(request):
    return HttpResponse("status ok")

def readiness(request):
    return HttpResponse("status ok")

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("health/", health),
    path("readiness/", readiness)
]

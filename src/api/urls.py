from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("ready", views.readiness),
    path("health", views.liveness),
    path("", include(router.urls))
]

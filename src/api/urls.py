from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views
from .views import health_check, readiness_check

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("health/", health_check, name="health-check"),
    path("ready/", readiness_check, name="readiness-check"),
]

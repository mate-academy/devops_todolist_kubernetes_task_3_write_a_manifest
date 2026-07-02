from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import liveness_check, readiness_check

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("liveness/", liveness_check, name="liveness_check"),
    path("readiness/", readiness_check, name="readiness_check"),
]

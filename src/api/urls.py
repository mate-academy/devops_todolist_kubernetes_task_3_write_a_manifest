from django.urls import include, path
from .views import readiness_view
from .views import liveness_view
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("readiness/", readiness_view),
    path("liveness/", liveness_view),
]

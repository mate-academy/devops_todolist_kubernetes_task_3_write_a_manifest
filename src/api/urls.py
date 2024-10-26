from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("health/", views.HealthCheckView.as_view(), name="health"),
    path("ready/", views.ReadyCheckView.as_view(), name="ready"),
]

urlpatterns += router.urls
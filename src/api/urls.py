from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import health_liveness, health_readiness

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("liveness/", health_liveness, name="liveness"),
    path("readiness/", health_readiness, name="readiness"),
]

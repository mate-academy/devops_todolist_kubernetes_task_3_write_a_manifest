from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views
from api.views import liveness_func, readiness_func

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("live", liveness_func, name="live-func"),
    path("read", readiness_func, name="read-func")
]

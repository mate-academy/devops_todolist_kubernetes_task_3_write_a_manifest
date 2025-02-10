from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import liveness_check, readiness_check, UserViewSet, TodoListViewSet, TodoViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"todolists", TodoListViewSet)
router.register(r"todos", TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("liveness/", liveness_check),
    path("readiness/", readiness_check)
]

from django.urls import include, path
from api.views import readiness_check, liveness_check
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("readiness/", readiness_check, name="readiness"),
    path("liveness/", liveness_check, name="liveness"),
    path("", include(router.urls)),
]

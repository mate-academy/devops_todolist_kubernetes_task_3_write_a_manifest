from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views
from api.views import readiness_view
from api.views import liveness_view

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("readiness/", readiness_view, name="readiness"),
    path("liveness/", liveness_view, name="liveness")
]

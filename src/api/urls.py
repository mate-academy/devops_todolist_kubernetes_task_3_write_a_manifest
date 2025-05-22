from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)



app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("healthcheck/", views.TodoHealthCheck.as_view(), name="healthcheck"),
    path("readinesscheck/", views.TodoReadinessCheck.as_view(), name="readinesscheck"),
]

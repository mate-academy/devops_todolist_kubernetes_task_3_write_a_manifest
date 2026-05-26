from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

from .views import live, ready

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path('healthz/live', live, name='live'),
    path('healthz/ready', ready, name='ready')
]

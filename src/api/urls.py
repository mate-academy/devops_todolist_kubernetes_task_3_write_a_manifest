from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views
from django.urls import path
from .views import readiness, liveness

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls))
]

urlpatterns += [
    path('readiness', readiness, name='readiness'),
    path('liveness', liveness, name='liveness'),
]

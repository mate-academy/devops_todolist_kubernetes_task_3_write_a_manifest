from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path('readiness/', views.readiness, name='readiness'),
    path('liveness/', views.liveness, name='liveness'),
]

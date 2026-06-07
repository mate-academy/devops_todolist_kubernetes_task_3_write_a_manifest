from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'lists', views.TodoListViewSet)
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Зверни увагу на кому в кінці рядка!

    path('healthz/liveness/', views.liveness_probe, name='liveness'),
    path('healthz/readiness/', views.readiness_probe, name='readiness'),
]

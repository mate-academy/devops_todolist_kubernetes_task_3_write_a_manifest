from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import readiness_check, liveness_check

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path('health/readiness/', readiness_check, name='readiness'),
    path('health/liveness/', liveness_check, name='liveness')
]

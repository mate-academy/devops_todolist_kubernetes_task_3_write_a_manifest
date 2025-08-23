from django.urls import path, include
from api.views import liveness_view, readiness_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# якщо маєш свої ViewSet-и — зареєструй їх тут:
# from api.views import TodoListViewSet
# router.register(r"todos", TodoListViewSet, basename="todos")

urlpatterns = [
    path("healthz/live", liveness_view, name="liveness"),
    path("healthz/ready", readiness_view, name="readiness"),
    path("", include(router.urls)),
]

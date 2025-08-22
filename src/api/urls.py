from django.urls import path, include
from rest_framework.routers import DefaultRouter

# імпортуй свої viewsets та health views
# приклад:
# from api.views import TodoListViewSet, liveness_view, readiness_view

router = DefaultRouter()
# приклад реєстрації твоїх viewsets:
# router.register(r'lists', TodoListViewSet, basename='lists')

urlpatterns = [
    path("healthz/live", liveness_view, name="liveness"),
    path("healthz/ready", readiness_view, name="readiness"),
    path("", include(router.urls)),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls))
]

from .views import liveness_view, readiness_view

urlpatterns = [
    path("healthz/live", liveness_view, name="liveness"),
    path("healthz/ready", readiness_view, name="readiness"),
    path("", include(router.urls)),   # залишаємо те, що в тебе було
]

from django.urls import path, include
from .views import liveness_view, readiness_view
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
# ... твої існуючі router.register(...)

urlpatterns = [
    path("healthz/live", liveness_view),
    path("healthz/ready", readiness_view),
    path("", include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from .views import liveness_view, readiness_view

router = DefaultRouter()
# ... твої router.register(...)

urlpatterns = [
    path("healthz/live", liveness_view, name="liveness"),
    path("healthz/ready", readiness_view, name="readiness"),
    path("", include(router.urls)),
]

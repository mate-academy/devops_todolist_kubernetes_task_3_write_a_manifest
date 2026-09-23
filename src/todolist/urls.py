from django.contrib import admin
from django.urls import include, path
from api import views as api_views

urlpatterns = [
    path("health/", api_views.liveness_check, name="liveness_check"),
    path("ready/", api_views.readiness_check, name="readiness_check"),
    path("", include("lists.urls")),
    path("auth/", include("accounts.urls")),
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
]

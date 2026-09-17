from django.contrib import admin
from django.urls import include, path
from api import views

urlpatterns = [
    path("", include("lists.urls")),
    path("auth/", include("accounts.urls")),
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    path("readiness_view", views.readiness),
    path("liveness_view", views.liveness),

]

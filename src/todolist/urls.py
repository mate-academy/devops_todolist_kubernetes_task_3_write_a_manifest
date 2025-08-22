from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("lists.urls")),
    path("auth/", include("accounts.urls")),
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
]

from django.urls import path, include

urlpatterns = [
    path("", include("api.urls")),
    # ... інші твої шляхи
]

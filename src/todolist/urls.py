from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # твої сторінки додатку:
    path("", include("lists.urls")),        # якщо є lists/urls.py
    path("auth/", include("accounts.urls")),# якщо є accounts/urls.py
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),      # <-- головне підключення API
]

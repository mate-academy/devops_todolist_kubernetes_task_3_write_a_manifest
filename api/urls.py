from django.urls import path
from . import views

urlpatterns = [
    # ... інші маршрути
    path('health/liveness/', views.liveness),
    path('health/readiness/', views.readiness),
]

from django.urls import path
from . import views

urlpatterns = [
    # ... інші маршрути
    path('liveness/', views.liveness),
    path('readiness/', views.readiness),
]

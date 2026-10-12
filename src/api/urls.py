from django.urls import path
from .views import liveness_probe, readiness_probe

urlpatterns = [
    # ... твої існуючі шляхи API ...
    path('healthz/live/', liveness_probe, name='liveness_probe'),
    path('healthz/ready/', readiness_probe, name='readiness_probe'),
]


from django.urls import path
from .views import liveness_probe, readiness_probe

urlpatterns = [
    # ... ваші існуючі шляхи API ...
    path('health/liveness/', liveness_probe, name='liveness_probe'),
    path('health/readiness/', readiness_probe, name='readiness_probe'),
]


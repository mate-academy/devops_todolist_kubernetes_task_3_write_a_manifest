from django.urls import path
from .views import liveness_check, readiness_check # Імпортуйте ваші нові views

urlpatterns = [
    # ... ваші наявні url-патерни ...
   path('healthz/live/', liveness_check, name='liveness_check'),
   path('healthz/ready/', readiness_check, name='readiness_check')]


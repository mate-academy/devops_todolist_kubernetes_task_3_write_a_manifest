from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api import views
from api.views import liveliness, readiness


router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

urlpatterns = [
 
    path("", include("lists.urls")),
    path("auth/", include("accounts.urls")),
    path("api/", include(router.urls)),  
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),

    path("readiness/", views.readiness, name="readiness"),
    path("liveliness/", views.liveliness, name="liveliness"),
]

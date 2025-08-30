from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from api.serializers import TodoListSerializer, TodoSerializer, UserSerializer
from lists.models import Todo, TodoList

from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.db import connections
from django.db.utils import OperationalError
import time

class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `creator` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # If the object doesn't have a creator (i.e. anon) allow all methods.
        if not obj.creator:
            return True

        # Instance must have an attribute named `creator`.
        return obj.creator == request.user


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class TodoListViewSet(viewsets.ModelViewSet):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsCreatorOrReadOnly,)

    def perform_create(self, serializer):
        user = self.request.user
        creator = user if user.is_authenticated else None
        serializer.save(creator=creator)

class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsCreatorOrReadOnly,)

    def perform_create(self, serializer):
        user = self.request.user
        creator = user if user.is_authenticated else None
        serializer.save(creator=creator)


def readiness_check(request):
    """
    Readiness probe endpoint - проверяет готовность приложения к обслуживанию запросов.
    Проверяет подключение к базе данных и основные зависимости.
    """
    try:
        # Проверяем подключение к базе данных
        db_conn = connections['default']
        db_conn.cursor()
        
        # Можно добавить дополнительные проверки здесь
        # Например, проверка внешних сервисов
        
        return JsonResponse({
            'status': 'ready',
            'timestamp': timezone.now().isoformat(),
            'checks': {
                'database': 'ok'
            }
        }, status=200)
    except OperationalError:
        return JsonResponse({
            'status': 'not ready',
            'timestamp': timezone.now().isoformat(),
            'checks': {
                'database': 'failed'
            }
        }, status=503)
    except Exception as e:
        return JsonResponse({
            'status': 'not ready',
            'timestamp': timezone.now().isoformat(),
            'error': str(e)
        }, status=503)


def liveness_check(request):
    """
    Liveness probe endpoint - проверяет, что приложение живо и отвечает.
    Простая проверка без тяжелых операций.
    """
    try:
        return JsonResponse({
            'status': 'alive',
            'timestamp': timezone.now().isoformat(),
            'uptime': time.time()
        }, status=200)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'timestamp': timezone.now().isoformat(),
            'error': str(e)
        }, status=500)
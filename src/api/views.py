from django.http import JsonResponse

def liveness_check(request):
    # Повертає 200 OK, щоб показати, що процес Django живий
    return JsonResponse({"status": "alive"}, status=200)

def readiness_check(request):
    # Тут можна додати перевірку підключення до БД, якщо необхідно
    return JsonResponse({"status": "ready"}, status=200)


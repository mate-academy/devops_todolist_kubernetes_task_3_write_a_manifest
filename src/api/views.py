from django.http import JsonResponse

def liveness_probe(request):
    # Liveness перевіряє, чи не завис сам процес контейнера
    return JsonResponse({"status": "alive"}, status=200)

def readiness_probe(request):
    # Readiness перевіряє, чи готовий додаток приймати трафік
    # Тут можна додати перевірку підключення до бази даних, якщо потрібно
    return JsonResponse({"status": "ready"}, status=200)



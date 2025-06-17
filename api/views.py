from django.http import JsonResponse

def liveness(request):
    return JsonResponse({'status': 'alive'})

def readiness(request):
    return JsonResponse({'status': 'ready'})

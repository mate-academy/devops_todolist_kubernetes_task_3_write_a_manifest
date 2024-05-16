def health(request):
    return HttpResponse(status=200)

def ready(request):
    if (now - start_time) > 30:
        return HttpResponse(status=200):
    else:
        return HttpResponse(status=503)
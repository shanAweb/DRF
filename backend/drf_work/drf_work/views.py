from django.http import JsonResponse

def root(request):
    return JsonResponse({
        "message": "Welcome to DRF from scratch",
        "status": "healthy",
        "/docs" : "API documentation"
    })
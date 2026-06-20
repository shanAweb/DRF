from django.http import JsonResponse

def api_view(request, *args, **kwargs):
    return JsonResponse({"message" : "Hi, Welcome to API"}
                        )
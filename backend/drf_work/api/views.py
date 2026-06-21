from django.http import JsonResponse
import json
def api_view(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return JsonResponse({"message" : "Invalid JSON"}, status = 400)
    return JsonResponse(data)
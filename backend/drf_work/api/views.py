from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiTypes

data = {}
@extend_schema(request=OpenApiTypes.OBJECT, responses=OpenApiTypes.OBJECT)
@api_view(['POST', 'GET'])
def endpoint_view(request, *args, **kwargs):
    global data
    body = request.body
    if request.method == 'POST':
        try:
            data = json.loads(body)
            return Response({"message" : "Message stored successfully"}, status=200)
        except json.JSONDecodeError:
            return Response({"message" : "Invalid JSON"}, status = 400)
    return Response(data)

@api_view(['GET'])
def get_status(*args, **kwargs):
    return Response({"status" : "ok"}, status=200)
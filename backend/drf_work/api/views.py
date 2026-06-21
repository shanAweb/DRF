from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiTypes

@extend_schema(request=OpenApiTypes.OBJECT, responses=OpenApiTypes.OBJECT)
@api_view(['POST'])
def endpoint_view(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return Response({"message" : "Invalid JSON"}, status = 400)
    return Response(data)
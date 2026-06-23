from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiTypes
from .models import Products

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

@api_view(['GET'])
def get_data(*args, **kwargs):
    fetched_data={}
    model_data = Products.objects.all().order_by("?").first()
    if model_data:
        fetched_data['id'] = model_data.id
        fetched_data['name'] = model_data.name
        fetched_data['price'] = model_data.price
        fetched_data['description'] = model_data.description
    return Response (fetched_data)
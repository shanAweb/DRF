from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiTypes
from .models import Products
from django.forms.models import model_to_dict
from .serializers import apiSerializer

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
        # fetched_data = model_to_dict(model_data, fields=['id', 'name', 'price', 'description'])
        fetched_data = apiSerializer(model_data).data
    return Response (fetched_data)
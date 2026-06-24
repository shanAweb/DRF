from rest_framework import serializers
from .models import Products

class apiSerializer (serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'name',
            'price',
            'description'
        ]
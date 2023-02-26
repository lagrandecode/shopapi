from rest_framework import serializers
from .models import ProductApi


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductApi
        fields = '__all__'
        depth = 1
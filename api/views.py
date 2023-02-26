from django.shortcuts import render
from rest_framework.response import Response
from api.models import ProductApi
from api.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.


@api_view(['GET','POST'])
def shop_list(request):
    if request.method == 'GET':
        api = ProductApi.objects.all()
        serializer = ProductSerializer(api,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





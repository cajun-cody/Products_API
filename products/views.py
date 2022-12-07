from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializers
from .models import Product


@api_view(['GET','POST']) #This decorator specifies what requests can be made. 
def products_list(request):    
    if request.method == 'GET':
        products = Product.objects.all() #Query to get all products
        serializer = ProductSerializers(products, many=True) #Many=True returns multiple
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT'])
def products_item(request,pk):
    product = get_object_or_404(Product, pk=pk) #Uses the django shortcuts import
    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializers(product, data=request.data) #Takes a look at the incoming data and compares it to the JSON data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
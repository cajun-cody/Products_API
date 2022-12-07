from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
        

@api_view(['GET'])
def products_item(request,pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
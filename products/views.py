from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializers
from .models import Product


@api_view(['GET','POST'])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def products_item(request,pk):


    return Response(f'ok{pk}')
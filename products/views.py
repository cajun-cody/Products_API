from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET','POST'])
def products_list(request):


    return Response('ok')


@api_view(['GET'])
def products_item(request,pk):


    return Response(f'ok{pk}')
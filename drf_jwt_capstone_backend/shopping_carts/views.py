from django.http.response import Http404
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer
from django.contrib.auth.models import User

# Create your views here.
class ProductList(APIView):
    
    permission_classes=[AllowAny]
    
    def get(self, request):
        shoppingcarts = ShoppingCart.objects.all()
        serializer = ShoppingCartSerializer(shoppingcarts, many=True)
        return Response(serializer.data)
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = ShoppingCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return ShoppingCart.objects.get(pk=pk)
        except ShoppingCart.DoesNotExist:
            raise Http404
    
    permission_classes = [AllowAny]

    #get by id
    def get(self, request, pk):
        shoppingcart = self.get_object(pk)
        serializer = ShoppingCartSerializer(shoppingcart)
        return Response(serializer.data)
    
    permission_classes = [AllowAny]

    #update
    def put(self, request, pk):
        shoppingcart = self.get_object(pk)
        serializer = ShoppingCartSerializer(shoppingcart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    permission_classes = [AllowAny]

    #delete
    def delete(self, request, pk):
        shoppingcart = self.get_object(pk)
        shoppingcart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

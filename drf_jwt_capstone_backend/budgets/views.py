from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Budget
from .serializers import BudgetSerializer
from django.contrib.auth.models import User

# Create your views here.
class BudgetList(APIView):
    
    permission_classes=[AllowAny]
    
    def get(self, request):
        budgets = Budget.objects.all()
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)
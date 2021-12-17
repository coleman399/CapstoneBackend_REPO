from django.urls import path
from budgets import views

urlpatterns = [
    path('', views.BudgetList.as_view())
]
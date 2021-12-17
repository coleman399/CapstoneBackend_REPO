from django.urls import path
from budgets import views

urlpatterns = [
    path('api/budgets/', views.BudgetList.as_view()),
    path('api/budgets/<int:pk>/', views.BudgetDetail.as_view()),
]
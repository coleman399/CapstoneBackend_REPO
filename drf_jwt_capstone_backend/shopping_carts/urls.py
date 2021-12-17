from django.urls import path
from shopping_carts import views

urlpatterns = [
    path('api/shoppingcarts/', views.ShoppingCartList.as_view()),
    path('api/shoppingcarts/<int:pk>/', views.ShoppingCartDetail.as_view()),
]
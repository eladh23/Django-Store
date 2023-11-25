from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from Supermarket import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='all_products'),
    path('products/<id>', views.product_detail, name="product_detail"),
    path('products/category/', views.get_one_categories, name='one_categories'),
    path('carts/', views.carts, name='carts'),
    path('carts/<id>', views.cart_detail, name="cart_detail"),
    path('cart_items/', views.cart_items, name='cart_items'),
    path('cart_items/<id>', views.cart_item_detail, name="cart_item_detail"),
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
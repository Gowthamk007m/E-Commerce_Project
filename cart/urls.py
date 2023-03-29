from django.urls import path
from . import views

urlpatterns = [
    path('add_cart/<int:product_id>/',views.Adding_cart,name="cart_add"),
    path('min_cart/<int:product_id>/',views.min_cart,name="min_cart"),
    path('delete_cart/<int:product_id>/',views.del_cart,name="del_cart"),
    path('cart_page/',views.cart_details,name='cart_page'),
    
]

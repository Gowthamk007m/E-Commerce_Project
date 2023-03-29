from django.urls import path

from . import views
from.views import *

urlpatterns = [
    path('new/',views.reverse,name='reverse'),
    path('<slug:c_slug>/q',views.new,name='new'),
    path('',views.display,name='front_view'),
    path('<slug:c_slug>/',views.product,name='product_page'),
    path('<slug:c_slug>/<slug:p_slug>', views.Prod_detail, name='Detail_page'),
    path('search',views.Searching,name='search_item'),
    


]

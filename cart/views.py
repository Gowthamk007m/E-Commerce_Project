from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from shop.models import *
from django.http import HttpResponse
from shop.urls import *

from accounts.views import *
from accounts.models import *

# Create your views here.


def cart_details(request,tot=0,count=0,cart_items=None,one=1):
    
    try:
        ct_items=None
        ct=CartData.objects.get(cart_id=create_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
           
            tot+=(i.prod.price*i.quan)
            count+=i.quan
        
    except ObjectDoesNotExist:
        pass
    
    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count,'on':one})


def create_id(request):
    ct_id = request.session.session_key
    if not request.session.session_key:
        request.session.create()
    ct_id = request.session.session_key
        
    return ct_id


def Adding_cart(request,product_id):

    prod_id = products.objects.get(id=product_id)
    
 

    try:
        data_pass_id = CartData.objects.get(cart_id=create_id(request))

    except CartData.DoesNotExist:
        data_pass_id = CartData.objects.create(cart_id=create_id(request))
        data_pass_id.save()

    try:
        c_items=items.objects.get(prod=prod_id,cart=data_pass_id)
        if c_items.quan < c_items.prod.stock:
            c_items.quan+=1
        c_items.save()
        
    except items.DoesNotExist:
        c_items=items.objects.create(prod=prod_id,quan=1,cart=data_pass_id)
        c_items.save()   

    

    return redirect('cart_page')


def min_cart(request,product_id):

    data_pass_id=CartData.objects.get(cart_id=create_id(request))
    prodt=products.objects.get(id=product_id)
    c_items=items.objects.get(prod=prodt,cart=data_pass_id)
    if c_items.quan > 1:
        c_items.quan-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart_page')




def del_cart(request,product_id):
  
    data_pass_id=CartData.objects.get(cart_id=create_id(request))
    prodt=products.objects.get(id=product_id)
    c_items=items.objects.filter(prod=prodt,cart=data_pass_id)
    c_items.delete()
    return redirect('cart_page')


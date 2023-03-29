from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import *
from django.views.generic import DetailView
import random
from accounts.models import *
# Create your views here.





def display(request):


    just = products.objects.all()
    category = categ.objects.all()
    bList=random.sample(list(just),12)
    

    return render(request, 'index.html', {'items': category, 'it':just,'random':bList})

def product(requset,c_slug):
    c_page=None
    prod=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prod=products.objects.filter(category=c_page, available=True)
    else:
        prod=products.objects.all().filter(available=True)

    paginator=Paginator(prod,8)
    try:
        page=int(requset.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(requset, 'products_sep.html', {'pr': prod,'pg':pro})





def Prod_detail(request,c_slug,p_slug):


    if User.is_authenticated:

        try:
            prod=products.objects.get(category__slug=c_slug,slug=p_slug)
        except Exception as e:
            raise e

        related_pro=products.objects.filter(category__slug=c_slug).exclude(slug=p_slug)


        related_pro=random.sample(list(related_pro),3)
    
    return render(request,'shop-single.html',{'i':prod,'related':related_pro})







def Searching(request):
    item=None
    query=None
    if 'search_area' in request.GET:
        query=request.GET.get('search_area')
        item=products.objects.all().filter(Q(name__contains=query))

    return render(request,'search.html',{'qr':query,'pr':item})

def reverse(request):
    just = products.objects.all()
    category = categ.objects.all()
    return render(request,'new.html', {'items': category, 'it':just})
    


def new(requset,p_slug,c_slug):

    
    return render(requset,'shop-single.html', {})
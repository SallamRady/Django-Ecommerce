from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product,Category
import ast
# Create your views here.

def listAll(request):
    productsInCart = ast.literal_eval(request.session['cart'])
    itemsCount = 0
    for k in productsInCart:
        itemsCount +=productsInCart[k]
    context = {
    'products':Product.objects.all().order_by('-create_at'),
    'categories':Category.objects.all(),
    'itemsCount':itemsCount
    }
    return render(request,'pages/home.html',context)



def product(request,id):
    try:
        productsInCart = ast.literal_eval(request.session['cart'])
        itemsCount = 0
        for k in productsInCart:
            itemsCount +=productsInCart[k]
        context = {
            'categories':Category.objects.all(),
            'product_id':id,
            'product':Product.objects.get(id=id),
            'itemsCount':itemsCount
        }
        return render(request,'pages/product.html',context)
    except:
        productsInCart = ast.literal_eval(request.session['cart'])
        itemsCount = 0
        for k in productsInCart:
            itemsCount +=productsInCart[k]
        context = {
        'products':Product.objects.all().order_by('-create_at'),
        'categories':Category.objects.all(),
        'itemsCount':itemsCount
        }
        return render(request,'pages/home.html',context)



def category(request,id):
    try:
        productsInCart = ast.literal_eval(request.session['cart'])
        itemsCount = 0
        for k in productsInCart:
            itemsCount +=productsInCart[k]
            
        cat = Category.objects.get(id=id)
        context = {
            'categories':Category.objects.all(),
            'category_id':id,
            'products':Product.objects.all().filter(category=id),
            'title':cat.name,
            'itemsCount':itemsCount
        }
        return render(request,'pages/Category.html',context)
    except:
        productsInCart = ast.literal_eval(request.session['cart'])
        itemsCount = 0
        for k in productsInCart:
            itemsCount +=productsInCart[k]
        context = {
        'products':Product.objects.all().order_by('-create_at'),
        'categories':Category.objects.all(),
        'itemsCount':itemsCount
        }
        return render(request,'pages/home.html',context)

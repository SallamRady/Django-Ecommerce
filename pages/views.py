from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from product.models import Category, Product
import ast
# Create your views here.

def index(request):
    if not request.session['cart']:
        request.session['cart'] = "{}"
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

def about(request):
    itemsCount = 0
    productsInCart = ast.literal_eval(request.session['cart'])
    itemsCount = 0
    for k in productsInCart:
        itemsCount +=productsInCart[k]
    context = {
    'itemsCount':itemsCount
    }
    return render(request,'pages/about.html',context)

def contact(request):
    itemsCount = 0
    productsInCart = ast.literal_eval(request.session['cart'])
    itemsCount = 0
    for k in productsInCart:
        itemsCount +=productsInCart[k]
    context = {
    'itemsCount':itemsCount
    }
    return render(request,'pages/contact.html',context)

def login(request):
    # request.session['logged'] = 1
    # del request.session['logged']
    if 'user_name' not in request.session:
        itemsCount = 0
        productsInCart = ast.literal_eval(request.session['cart'])
        itemsCount = 0
        for k in productsInCart:
            itemsCount +=productsInCart[k]
        context = {
        'itemsCount':itemsCount
        }
        return render(request,'pages/login.html',context)
    else:
        if not request.session['cart']:
            request.session['cart'] = "{}"
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

def login_process(request):
    if request.method == 'POST' and 'name' and 'password' in request.POST:
        request.session['user_name'] = request.POST['name']
        request.session['user_password'] = request.POST['password']
        request.session['cart'] = "{}"

        if not request.session['cart']:
            request.session['cart'] = "{}"
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
    else:
        itemsCount = 0
        productsInCart = ast.literal_eval(request.session['cart'])
        itemsCount = 0
        for k in productsInCart:
            itemsCount +=productsInCart[k]
        context = {
        'itemsCount':itemsCount
        }
        return render(request,'pages/login.html',context)


def logout(request):
    if 'user_name' in request.session:
        del request.session['user_name']
        del request.session['user_password']
        del request.session['cart']
    
    request.session['cart'] = "{}"
    itemsCount = 0
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

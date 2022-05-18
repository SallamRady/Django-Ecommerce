from unicodedata import decimal
from django.http import HttpResponseRedirect
from django.shortcuts import render
from product.models import Category, Product
import json
import ast
# Create your views here.
def addProduct(request):
    if 'user_name' in request.session and request.method == 'POST' and 'id' in request.POST:
        id = request.POST['id']
        if not request.session['cart']:
            request.session['cart'] = "{}"

        # convert string to dictionary
        productsInCart = ast.literal_eval(request.session['cart'])
        # add product to products in cart
        if id in productsInCart:
            productsInCart[id] +=1
        else:
            productsInCart[id] = 1

        itemsCount = 0
        for k in productsInCart:
            itemsCount +=productsInCart[k]
        request.session['cart'] = str(productsInCart)
        # stay at home page
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


def removeProduct(request):
    id = request.POST['id']
    if not request.session['cart']:
        request.session['cart'] = "{}"

    # convert string to dictionary
    productsInCart = ast.literal_eval(request.session['cart'])
    # remove product to products in cart
    if id in productsInCart:
        productsInCart.pop(id)
        # del productsInCart[id]
        
    ids=list(productsInCart.keys())
    itemsCount = 0
    for k in productsInCart:
        itemsCount +=productsInCart[k]
    products = Product.objects.filter(id__in = ids)
    total = 0.0
    for pro in products:
        # pro.amount
        total +=(float(pro.price))
        # print(type(productsInCart[int(pro.id)]))
    request.session['cart'] = str(productsInCart)
    context = {
    'products':products,
    'categories':Category.objects.all(),
    'itemsCount':itemsCount,
    'total':total
    }
    return render(request,'pages/checkOut.html',context)

def checkout(request):
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
        # go to check out page
        productsInCart = ast.literal_eval(request.session['cart'])
        ids=list(productsInCart.keys())
        print('------------')
        print(productsInCart)
        itemsCount = 0
        for k in productsInCart:
            itemsCount +=productsInCart[k]
        products = Product.objects.filter(id__in = ids)
        total = 0.0
        for pro in products:
            # pro.amount
            total +=(float(pro.price))
            # print(type(productsInCart[int(pro.id)]))

        context = {
        'products':products,
        'categories':Category.objects.all(),
        'itemsCount':itemsCount,
        'total':total
        }
        return render(request,'pages/checkOut.html',context)
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Cart, Category, Product
from django.db.models import Q




# Create your views here.

# def home(request):
#     return render(request, 'shop/home.html')

def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    cart = Cart.objects.all()

    context = {'category':category, 'cart':cart, 'products':products,}

    return render(request, 'shop/home.html', context)

def add_to_cart(request):
    user=request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('home')

    



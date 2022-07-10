from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def categories(request):
    return {
        'categories': Category.objects.all() # dodalem to do templates w settings
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, slug): #slug daje zeby wywolac poszczegolny produkt
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'detail.html', {'product': product})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})
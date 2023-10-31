from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import *

# Create your views here.
class ViewAllProducts(View):
    def get(self, request):
        products = Product.objects.all()

        context = {
            'title': 'Список продуктов',
            'products': products,
        }
        
        return render(request, 'products/index.html', context=context)

class ProductDetails(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except:
            return HttpResponse('Product not found')
        
        # res = f'ID: {product.id}<br>Название продукта: {product.name}<br>Описание продукта: {product.description if product.description else "Пусто"}<br>Цена: {product.price} KZT'
        # return HttpResponse(res)

        context = {
            'title': 'Описание продукта',
            'product': product,
        }
    
        return render(request, 'products/details.html', context=context)

class ViewProductsByCategory(View):
    def get(self, request, category_id):
        products = Product.objects.filter(category_id=category_id)
        res = ''

        for p in products:
            res += f'#{p.id}, Название: {p.name}, Категория: {p.category.name}<br>'

        if not res:
            return HttpResponse('Данная категория не имеет продуктов')
        else:
            return HttpResponse(res)
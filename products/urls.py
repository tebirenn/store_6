from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.ViewAllProducts.as_view(), name='index'),
    path('products/<int:product_id>/', views.ProductDetails.as_view()),
    path('products/category/<int:category_id>/', views.ViewProductsByCategory.as_view()),
]

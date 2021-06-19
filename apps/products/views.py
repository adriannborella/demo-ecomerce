from django.views.generic import TemplateView
from rest_framework import viewsets
from apps.products.models import Category, Product
from apps.products.serializer import CategorySerializer, ProductSerializer
from rest_framework.permissions import AllowAny

class IndexView(TemplateView):
    template_name = 'index.html'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
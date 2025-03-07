from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .forms import ProductForm
from .forms import Product
# Create your views here.

class ProducFormView(generic.FormView):
    template_name = "products/add_products.html"
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save ()
        return super().form_valid(form)

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list_products.html'
    context_object_name = 'products'

class ProductListAPI(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request):
        products = Product. objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class AdminProducts(generic.ListView):
    model = Product
    template_name = 'products/admin_products.html'
    context_object_name = 'products'
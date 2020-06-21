from django.shortcuts import render
from django.utils import timezone
from .models import products as productdata
from django.contrib import messages

# Create your views here.
def index(request):
    productsdata = productdata.objects.all()
    param={'productsdata':productsdata}
    return render(request,'products/index.html',param)

def addproduct(request):
    if request.method == "POST":
        product_name = request.POST.get('name', '')
        weight = request.POST.get('weight', '')
        price = request.POST.get('price', '')
        if product_name=='' or weight=='' or price=='':
            messages.error(request, 'Please fill the form correctly.')
        else:
            data = productdata(product_name=product_name, weight=weight, price=price)
            data.save()
            messages.success(request, f'{product_name} Added Successfully.')
    return render(request,'products/addproduct.html')

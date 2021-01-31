from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PagesForm
import subprocess
import sys
import re
from urllib.request import urlretrieve 
from requests.utils import requote_uri 
python_path = sys.executable
from os.path import abspath, dirname, join
 

def get_price(item, zip_code):
    
    merchant='walmart'
    price='12.99'
    url='https://www.nescafe.com/sites/default/files/styles/product_recommendation_large/public/2020-04/NESCAF%C3%89%20Classic_0.png?itok=xEQ6xzPZ'

    return merchant,price,url

# Create your views here.
def homePageView(request):
    if request.method == "POST":
        filled_form = PagesForm(request.POST)
        if filled_form.is_valid():
            note = "Thank you! Your %s is  \
            loading!" %(filled_form.cleaned_data['item_name'],)
            new_form = PagesForm()
        return render(request, 'pages/home.html',{'pagesform':new_form,'note':note})
    
    else:
        form = PagesForm()
        return render(request,'pages/home.html',{'pagesform':form})    

def processView(request):
    context={}
    print('*'*30)
    print(request)
    item = request.POST.get('item_name')
    print(item)
    zipcode = request.POST.get('zip_code')
    merchant, price, imgurl = get_price(item, zipcode)
    context['price'] = price
    context['merchant'] = merchant
    context['img'] = imgurl
    context['item'] = item

    return render(request, 'pages/process.html', context)   


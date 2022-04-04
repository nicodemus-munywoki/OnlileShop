from django.shortcuts import render
from django.http import HttpResponse
from .models import Productss
# Create your views here.

def index(request):
    
    
    prods = Productss.objects.all()
    
    return render(request, 'index.html',{'prodct' : prods})
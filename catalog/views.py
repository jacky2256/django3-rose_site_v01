from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'catalog/home.html')


def catalog(request):
    return render(request, 'catalog/catalog.html')

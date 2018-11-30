from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Test

def index(request):
    return render(request, 'home.html')

def show(request):
    table=Test.objects.all()
    return render(request, 'table.html',locals())
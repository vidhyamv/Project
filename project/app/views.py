
from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, space


# Create your views here.

def demo(request):
    obj1=Place.objects.all()
    obj2=space.objects.all()
    return render(request,"index.html",{'result':obj1,'output':obj2})



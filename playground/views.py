from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cal():
    x= 1
    y = 2
    return x, y 

def say_hello(request):
    x = cal()
    return render(request, 'hello.html', {'name': 'Khải'})

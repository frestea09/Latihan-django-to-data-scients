from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,'about.html')
def index2(request):
    return render(request,'index.html')
def index(request):
    return HttpResponse("<h1>Hello World</h1>")
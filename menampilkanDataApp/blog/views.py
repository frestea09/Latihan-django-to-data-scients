from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    posts = models.Blog.objects.all()
    context={
        'post':posts,
    }
    return render(request,'base.html',context)
from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    data = models.Blog.objects.all()
    content = {
        'data':data,
    }
    return render(request,'blog/base.html',content)
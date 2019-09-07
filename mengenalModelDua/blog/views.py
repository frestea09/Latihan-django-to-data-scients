from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    posts = models.Blog.objects.all()
    content = {
        'posts':posts,
        'namePage': 'Blog',
        'title': 'Selamat Datang DiBlog',
        'nav': [
            ['/home/', 'Article 1'],
            ['/about/', 'Article 2'],
            ['/blog/', 'Article 3'],
        ]
    }
    return render(request,'blog/index.html',content)
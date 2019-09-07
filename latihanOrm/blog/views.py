from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    posts = models.Blog.objects.all()
    data = {
        'title':'Welcome in Blog',
        'content':'berikut adalah article yang tersedia sekarang.',
        'posts':posts,
        'nav':[
            ['/blog/', 'All'],
            ['/blog/article/', 'Article'],
            ['/blog/jurnal/', 'Journal'],
            ['/blog/draf/', 'Draf'],
        ],
    }
    return render(request,'blog/index.html',data)
def article(request):
    posts = models.Blog.objects.filter(category='article')
    data = {
        'title': 'Welcome in Blog',
        'content': 'berikut adalah article yang tersedia sekarang.',
        'posts': posts,
        'nav': [
            ['/blog/', 'All'],
            ['/blog/article/', 'Article'],
            ['/blog/jurnal/', 'Journal'],
            ['/blog/draf/', 'Draf'],
        ],
    }
    return render(request, 'blog/index.html', data)
def jurnal(request):
    posts = models.Blog.objects.filter(category='jurnal')
    data = {
        'title': 'Welcome in Blog',
        'content': 'berikut adalah article yang tersedia sekarang.',
        'posts': posts,
        'nav': [
            ['/blog/', 'All'],
            ['/blog/article/', 'Article'],
            ['/blog/jurnal/', 'Journal'],
            ['/blog/draf/', 'Draf'],
        ],
    }
    return render(request, 'blog/index.html', data)
def draf(request):
    posts = models.Blog.objects.filter(category='draf')
    data = {
        'title': 'Welcome in Blog',
        'content': 'berikut adalah article yang tersedia sekarang.',
        'posts': posts,
        'nav': [
            ['/blog/', 'All'],
            ['/blog/article/', 'Article'],
            ['/blog/jurnal/', 'Journal'],
            ['/blog/draf/', 'Draf'],
        ],
    }
    return render(request, 'blog/index.html', data)
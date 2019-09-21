from django.shortcuts import render
from datetime import date
from . import models
# Create your views here.
def index(request):
    today = date.today()
    myData = models.Blog.objects.all()
    content = {
        'judul':'Selamat Datang di Blog',
        'author':'ilman teguh prasetya',
        'content':'ini adalah bagian model',
        'today':today,
        'myData':myData,
        'nav':[
            ['/jurnal/','Jurnal'],
            ['/jurnal/','Draf'],
            ['/jurnal/','Article'],
            ['/jurnal/','Jurnal'],
        ]
    }
    return render(request,'blog/index.html',content)
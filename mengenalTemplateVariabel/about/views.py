from django.shortcuts import render
from datetime import date
# Create your views here.
def index(request):
    today = date.today()
    context = {
        'judul': 'About',
        'author': 'ilman teguh prasetya',
        'date': today,
        'deskripsi': 'Tell who develop this website.',
        'nav': [
            ['/', 'Home'],
            ['/about/', 'About'],
            ['/blog/', 'Blog'],
        ],
    }
    return render(request,'about/index.html',context)
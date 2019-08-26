from django.shortcuts import render
from datetime import date
def index(request):
    today = date.today()
    context = {
        'judul':'Sambutan',
        'author':'ilman teguh prasetya',
        'date': today,
        'deskripsi':'description for user who user this page.',
        'nav':[
            ['/','Home'],
            ['/about/','About'],
            ['/blog/','Blog'],
        ],
    }
    return render(request,'index.html',context)
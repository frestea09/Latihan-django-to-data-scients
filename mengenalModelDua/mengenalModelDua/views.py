from django.shortcuts import render

def index(request):
    content = {
        'title':'Selamat Data',
        'posts':[
            ['title','hello world'],
            ['post','hallo ini post saya'],
        ],
        'nav':[
            ['/home/','Home'],
            ['/about/','About'],
            ['/blog/','Blog'],
        ]
    }
    return render(request,'index.html',content)
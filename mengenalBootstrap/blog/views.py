from django.shortcuts import render
from datetime import date
# Create your views here.
def index(request):
    today = date.today()
    context = {
        'judul': 'Blog',
        'author': 'ilman teguh prasetya',
        'date': today,
        'styles': 'snippets/styles.html',
        'navbar': 'snippets/navbar.html',
        'jumbroton': 'snippets/jumbroton.html',
        'javascripts': 'snippets/javascripts.html',
        'css': 'css/styles.css',
        'bootstrapCss': 'vendor/bootstrap-4.3.1-dist/css/bootstrap.min.css',
        'bootStrapJsBootstrap': 'vendor/bootstrap-4.3.1-dist/js/bootstrap.min.js',
        'bootStrapJsPopper': 'vendor/bootstrap-4.3.1-dist/js/popper.min.js',
        'bootStrapJsSlim': 'vendor/bootstrap-4.3.1-dist/js/jquery-3.3.1.slim.min.js',

    }
    return render(request,'blog/index.html',context)

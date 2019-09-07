from django.shortcuts import render
from datetime import date
def index(request):
    today = date.today()
    data = {
        'title':'Pertama',
        'content':'ini pertama',
        'author':'ilman teguh prasetya',
        'date':today,
    }
    return render(request,'index.html',data)
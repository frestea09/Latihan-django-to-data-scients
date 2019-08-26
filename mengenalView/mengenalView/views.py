from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>ini adalah index</h1>")
def about(request):
    return HttpResponse("<h1>ini adalah About")
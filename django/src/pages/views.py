from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>This is the homepage.</h1>")

def info_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "info.html", {})

def context_view(request, *args, **kwargs):
    premade_context = {
            "text": "This string was premade.",
            "number": 123456,
            "my_list": ['element1','element2','element3']
            
    }

    return render(request, "context.html", premade_context)

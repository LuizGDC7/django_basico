from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    print("blog")
    return render(request,"blog/index.html")

def subBlog(request):
    print("Superblog!")
    return HttpResponse("Superblog1!")

def subsubBlog(request):
    print("Superblog!")
    return HttpResponse("Superblog1!")

# Create your views here.

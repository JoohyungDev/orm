from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "main/index.html")


def a(request):
    return render(request, "main/a.html")


def b(request):
    return render(request, "main/b.html")


def c(request):
    return render(request, "main/c.html")


def hojun(request):
    return render(request, "main/hojun.html")


def orm(request):
    return render(request, "main/orm.html")
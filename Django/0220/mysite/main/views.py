from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def notice(request):
    return render(request, "notice.html")


def notice1(request):
    return render(request, "notice1.html")


def notice2(request):
    return render(request, "notice2.html")


def notice3(request):
    return render(request, "notice3.html")


def contact(request):
    return render(request, "contact.html")


def abcd(request):
    return render(request, "abcd.html")


def hojun(request):
    return render(request, "hojun.html")


def mini(request):
    return render(request, "mini.html")
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def product(request):
    return HttpResponse("상품 목록")


def productdetails(request, pk):
    return HttpResponse(f"상품 목록 상세 게시물 {pk}번")

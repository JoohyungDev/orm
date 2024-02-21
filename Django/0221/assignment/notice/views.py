from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def notice(request):
    return HttpResponse("자유게시판")


def noticefree(request):
    return HttpResponse("자유게시판 목록")


def noticefree_details(request, pk):
    return HttpResponse(f"자유게시판 상세 게시물 {pk}번")


def onenone(request):
    return HttpResponse("1:1 상담 안내")


def onenone_details(request, pk):
    return HttpResponse(f"1:1 상담 상세 게시물 {pk}번")

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def qna(request):
    return HttpResponse("QnA 목록")


def qnadetails(request, pk):
    return HttpResponse(f"QnA 상세 게시물 {pk}번")

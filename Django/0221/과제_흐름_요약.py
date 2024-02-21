# tutorial > urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # ""URL로 들어오면 main앱에 urls.py로 연결하겠다.
    path("", include("main.urls")),
    # product/"URL로 들어오면 product앱에 urls.py로 연결하겠다.
    path("product/", include("product.urls")),
    # qna/"URL로 들어오면 qna앱에 urls.py로 연결하겠다.
    path("qna/", include("qna.urls")),
    # notice/"URL로 들어오면 notice앱에 urls.py로 연결하겠다.
    path("notice/", include("notice.urls")),
]

# main > urls.py
from django.urls import path
from .views import index, about, contact

urlpatterns = [
    path("", index),  # 잘 나가는 상품 10개 소개 페이지(메인)
    path("about/", about),  # 회사 소개
    path("contact/", contact),  # 오시는 길
]


# main > views.py
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("잘 나가는 상품 10개 소개")


def about(request):
    return HttpResponse("회사 소개")


def contact(request):
    return HttpResponse("오시는 길")


# notice > urls.py
from django.urls import path
from .views import notice, noticefree, noticefree_details, onenone, onenone_details

urlpatterns = [
    path("", notice),  # 자유게시판, 1:1 게시판 선택 페이지
    path("free/", noticefree),  # 자유게시판 목록
    path("free/<int:pk>/", noticefree_details),  # 자유게시판 상세 게시물
    path("onenone/", onenone),  # 1:1 상담 안내
    path("onenone/<int:pk>/", onenone_details),  # 1:1 상담 상세 게시물
]

# notice > views.py
from django.shortcuts import render
from django.http import HttpResponse


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


# product > urls.py
from django.urls import path
from .views import product, productdetails

urlpatterns = [
    path("", product),  # 상품 목록
    path("<int:pk>/", productdetails),  # 상품 목록 상세 게시물
]

# product > views.py
from django.shortcuts import render
from django.http import HttpResponse


def product(request):
    return HttpResponse("상품 목록")


def productdetails(request, pk):
    return HttpResponse(f"상품 목록 상세 게시물 {pk}번")


# qna > urls.py
from django.urls import path
from .views import qna, qnadetails

urlpatterns = [
    path("", qna),  # Q&A 목록
    path("<int:pk>/", qnadetails),  # Q&A 상세 게시물
]

# qna > views.py
from django.shortcuts import render
from django.http import HttpResponse


def qna(request):
    return HttpResponse("QnA 목록")


def qnadetails(request, pk):
    return HttpResponse(f"QnA 상세 게시물 {pk}번")

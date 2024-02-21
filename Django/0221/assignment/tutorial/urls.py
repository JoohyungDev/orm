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

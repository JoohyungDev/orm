from django.urls import path
from .views import index, about

urlpatterns = [
    # 사용자가 페이지를 방문하면, 해당 메세지를 포함하는 응답 반환
    path("", index, name="index"),
    path("about/", about, name="about"),
]

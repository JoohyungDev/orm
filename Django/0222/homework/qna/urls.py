from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    # 사용자가 페이지를 방문하면, 해당 메세지를 포함하는 응답 반환
    path("", lambda request: HttpResponse("Helllo, world! qna index")),
    path(
        "<int:pk>/", lambda request, pk: HttpResponse("Helllo, world! about qna detail")
    ),
]

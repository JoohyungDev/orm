from django.urls import path
from .views import qna, qnadetails

urlpatterns = [
    path("", qna),
    path("<int:pk>/", qnadetails),
]

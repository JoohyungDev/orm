from django.urls import path
from .views import product_index, product_detail

urlpatterns = [
    # 사용자가 페이지를 방문하면, 해당 메세지를 포함하는 응답 반환
    path("", product_index, name="product_index"),
    path("<int:pk>/", product_detail, name="product_detail"),
]

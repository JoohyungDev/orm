from django.urls import path
from .views import product, productdetails

urlpatterns = [
    path("", product),
    path("<int:pk>/", productdetails),
]

from django.urls import path
from .views import notice, noticefree, noticefree_details, onenone, onenone_details

urlpatterns = [
    path("", notice),
    path("free/", noticefree),
    path("free/<int:pk>/", noticefree_details),
    path("onenone/", onenone),
    path("onenone/<int:pk>/", onenone_details),
]

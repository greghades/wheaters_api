from django.urls import path
from .views import Get_Wheaters_Cities

urlpatterns = [
    path("forecast/daily/",Get_Wheaters_Cities.as_view()),
]
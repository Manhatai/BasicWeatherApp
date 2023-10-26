from django.urls import path
from WeatherApp import views

urlpatterns = [
    path("WeatherApp/", views.temp_here, name="temp_here"),
    path("WeatherApp/discover", views.temp_somewhere, name="temp_somewhere")

]

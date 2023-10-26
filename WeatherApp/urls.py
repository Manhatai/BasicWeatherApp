from django.urls import path
from WeatherApp  import views

urlpatterns = [
    path("WeatherApp/", views.temp_here, name="temp_here")
]
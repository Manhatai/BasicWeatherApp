import datetime
import geocoder
import requests
from django.http import HttpResponse
from django.template import loader
from WeatherApp.models import Worldcities


def temp_somewhere(request):
    random_item = Worldcities.objects.all().order_by('?').first()
    city = random_item.city
    country = random_item.country
    location = [random_item.lat, random_item.lng]
    temp = get_temp(location)
    template = loader.get_template('index.html')
    context = {
        'city': city,
        'country': country,
        'temp': temp
    }
    return HttpResponse(template.render(context, request))


def temp_here(request):
    location_latlng = geocoder.ip('me').latlng
    city = 'Your location'
    temp = get_temp(location_latlng)
    template = loader.get_template('index.html')
    context = {
        'city': city,
        'temp': temp
    }
    return HttpResponse(template.render(context, request))


def get_temp(location):
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    now = datetime.datetime.now()
    hour = now.hour
    meteo_data = requests.get(api_request).json()
    temp = meteo_data['hourly']["temperature_2m"][18]
    return temp

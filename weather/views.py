from django.shortcuts import render
import requests
from .forms import CityForm

def weather_view(request):
    api_key = "7ba4c3f33386401b4caaacefb4cfa4b5"  
    url = "http://api.openweathermap.org/data/2.5/weather"
    weather_data = {}
    form = CityForm()

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city_name']
            params = {'q': city, 'appid': api_key, 'units': 'metric'}
            response = requests.get(url, params=params)
            if response.status_code == 200:
                weather_data = response.json()

    return render(request, 'weather/weather.html', {'form': form, 'weather_data': weather_data})


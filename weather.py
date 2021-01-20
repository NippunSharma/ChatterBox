import requests
import json


def currentWeather(city):
    key_url = f"http://dataservice.accuweather.com/locations/v1/cities/search.json?q={city}&apikey=JfVLUjQq1dn67mUZQau8SCFEYXr0e5j8&language=en-us"
    response = requests.get(key_url)
    a = json.loads(response.content)
    key = a[0]['Key']
    base_url = "http://dataservice.accuweather.com/currentconditions/v1/" + \
        key+"?apikey=JfVLUjQq1dn67mUZQau8SCFEYXr0e5j8"
    response = requests.get(base_url)
    b = json.loads(response.content)

    weather = b[0]['WeatherText']

    precipitation = ""
    if (b[0]['HasPrecipitation']):
        if(b[0]['PrecipitationType'] == 'Rain'):
            precipitation = "It is raining now!"
        elif (b[0]['PrecipitationType'] in ['Snow', 'Ice', 'Mixed']):
            precipitation = "Currently, it's snowing!"

    temperature_in_c = str(b[0]['Temperature']['Metric']['Value']) + " °C"
    temperature_in_f = str(b[0]['Temperature']['Imperial']['Value']) + " °F"

    response = f"The weather conditions at {city} : {weather}.\nCurrent temperature : {temperature_in_c} / {temperature_in_f}.\n{precipitation}"
    return response

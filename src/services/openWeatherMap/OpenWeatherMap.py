import requests

from src import config
from src.services.openWeatherMap.DayHourForecast import DayHourForecast
from src.services.openWeatherMap.LocationForecast import LocationForecast


### function: getForecast ###

def getForecast (city, days) : # free version: 5 days - 3 hours
    apiCityCall = config.API_BASE_CALL + "&q=" + city
    jsonResponse = requests.get (apiCityCall).json ()

    forecasts = []

    for blockForecastInfo in jsonResponse ['list'] :
        originalDate, hour = blockForecastInfo ['dt_txt'].split (' ')

        date = originalDate.replace ("-", "")
        hour = hour [:5]

        weather = blockForecastInfo ['weather'] [0] ['main']
        weatherDescription = blockForecastInfo ['weather'] [0] ['description']

        temperature = '{:.2f}'.format (blockForecastInfo ['main'] ['temp'] - 273)
        minimTemperature = '{:.2f}'.format (blockForecastInfo ['main'] ['temp_min'] - 273)
        maximTemperature = '{:.2f}'.format (blockForecastInfo ['main'] ['temp_max'] - 273)

        pressure = str (blockForecastInfo ['main'] ['pressure'])
        humidity = str (blockForecastInfo ['main'] ['humidity'])

        windSpeed = str (blockForecastInfo ['wind'] ['speed'])

        forecasts.append (DayHourForecast (date,
                                           hour,
                                           weather,
                                           weatherDescription,
                                           temperature,
                                           minimTemperature,
                                           maximTemperature,
                                           pressure,
                                           humidity,
                                           windSpeed))

    latitude = str (jsonResponse ['city'] ['coord'] ['lat'])
    longitude = str (jsonResponse ['city'] ['coord'] ['lon'])
    country = jsonResponse ['city'] ['country']
    cityName = jsonResponse ['city'] ['name']
    timezone = str (jsonResponse ['city'] ['timezone'])

    return LocationForecast (latitude, longitude, country, cityName, timezone, forecasts)
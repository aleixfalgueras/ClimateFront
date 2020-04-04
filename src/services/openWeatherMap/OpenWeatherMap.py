import logging
from datetime import datetime

import requests

from src import config
from src.api_rest.model.entity.EntityDayHourForecast import EntityDayHourForecast
from src.api_rest.model.entity.EntityLocationForecast import EntityLocationForecast


### function: getCityId ###

def getCityId (codeIATACity) :
    try:
        if   codeIATACity == "BCN" : return "3128760"
        elif codeIATACity == "LON" : return "2643743"
        else:
            raise Exception ("Unknow city IATA code")

    except Exception as exc :
        logging.error ("OpenWeatherMap: getCityId: Error getting id of city IATA code: " + codeIATACity)
        logging.error ("[Exception: " + str (exc) + "]")


### function: getForecast ###

def getCityForecast (codeIATACity, startDay = datetime.now ().strftime ("%Y%m%d"), days = 5, hours = 3) :
    try:
        cityId = getCityId (codeIATACity)

        apiCityCall  = config.API_BASE_CALL + "&id=" + cityId
        jsonResponse = requests.get (apiCityCall).json ()

        latitude  = str (jsonResponse ['city'] ['coord'] ['lat'])
        longitude = str (jsonResponse ['city'] ['coord'] ['lon'])
        country   = jsonResponse ['city'] ['country']
        cityName  = jsonResponse ['city'] ['name']
        timezone  = str (jsonResponse ['city'] ['timezone'])

        dayHourForecasts = []

        for forecastInfo in jsonResponse ['list'] :
            date, hour = forecastInfo ['dt_txt'].split (' ')

            date = date.replace ("-", "")
            hour = hour [:5]

            weather            = forecastInfo ['weather'] [0] ['main']
            weatherDescription = forecastInfo ['weather'] [0] ['description']

            temperature      = '{:.2f}'.format (forecastInfo ['main'] ['temp'] - 273)
            minimTemperature = '{:.2f}'.format (forecastInfo ['main'] ['temp_min'] - 273)
            maximTemperature = '{:.2f}'.format (forecastInfo ['main'] ['temp_max'] - 273)

            pressure = str (forecastInfo ['main'] ['pressure'])
            humidity = str (forecastInfo ['main'] ['humidity'])

            windSpeed = str (forecastInfo ['wind'] ['speed'])

            dayHourForecasts.append (EntityDayHourForecast (
                                                     date,
                                                     hour,
                                                     weather,
                                                     weatherDescription,
                                                     temperature,
                                                     minimTemperature,
                                                     maximTemperature,
                                                     pressure,
                                                     humidity,
                                                     windSpeed))

        return EntityLocationForecast (latitude, longitude, country, cityName, timezone, dayHourForecasts)

    except Exception as exc :
        logging.error ("OpenWeatherMap: getCityForecast: Error getting forcasts for the city IATA code: " + codeIATACity)
        logging.error ("[Exception: " + str (exc) + "]")

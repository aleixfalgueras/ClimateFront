import logging

import requests

from src import config
from src.api_rest.model.entity.EntityDayHourForecast import EntityDayHourForecast
from src.api_rest.model.entity.EntityLocationForecast import EntityLocationForecast


### function: getCityId ###

def getCityId (codeIATACity):
    try:
        if codeIATACity == "BCN": return "3128760"
        elif codeIATACity == "LON": return "2643743"
        else:
            raise Exception ("Unknow city")

    except Exception as exc :
        logging.error ("OpenWeatherMap: getCityId: Error getting id of city with IATA code: " + codeIATACity)
        logging.error ("[Exception: " + str (exc) + "]")


### function: getForecast ###

def getForecast (codeIATACity, days = 5, hours = 3) : # free version: 5 days - 3 hours
    try:

        cityId = getCityId (codeIATACity)

        apiCityCall = config.API_BASE_CALL + "&id=" + cityId
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

            forecasts.append (EntityDayHourForecast (date,
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

        return EntityLocationForecast (latitude, longitude, country, cityName, timezone, forecasts)

    except Exception as exc:
        logging.error ("OpenWeatherMap: getForecast: Error getting forcasts for the city with IATA code: " + codeIATACity)
        logging.error ("[Exception: " + str (exc) + "]")

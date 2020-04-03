from src.commons import MongoLocationForecast


################################################################################
# class: EntityLocationForecast
################################################################################

class EntityLocationForecast :

    ENTITY_NAME = "LocationForecast"


    ### function: __init__ ###

    def __init__ (self, latitude, longitude, country, city, timezone, dayHourForecasts) :
        self.latitude = latitude
        self.longitude = longitude
        self.country = country
        self.city = city
        self.timezone = timezone
        self.dayHourForecasts = dayHourForecasts

        self.startForecast = dayHourForecasts [0].date + " " + dayHourForecasts [0].hour
        self.endForecast = dayHourForecasts [len (dayHourForecasts) - 1].date + " " + dayHourForecasts [len (dayHourForecasts) - 1].hour


    ### function: toJson ###

    def toJson (self) :
        dayHourForecastsJsons = []

        for dayHourForecast in self.dayHourForecasts : dayHourForecastsJsons.append (dayHourForecast.toJson ())

        return {
            MongoLocationForecast.LATITUDE : self.latitude,
            MongoLocationForecast.LONGITUDE : self.longitude,
            MongoLocationForecast.COUNTRY : self.country,
            MongoLocationForecast.CITY : self.city,
            MongoLocationForecast.TIMEZONE : self.timezone,
            MongoLocationForecast.START_FORECAST : self.startForecast,
            MongoLocationForecast.END_FORECAST : self.endForecast,
            MongoLocationForecast.DAY_HOUR_FORECASTS : dayHourForecastsJsons
        }
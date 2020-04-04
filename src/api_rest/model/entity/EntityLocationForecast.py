from src.commons import MongoLocationForecastFields


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
            MongoLocationForecastFields.LATITUDE : self.latitude,
            MongoLocationForecastFields.LONGITUDE : self.longitude,
            MongoLocationForecastFields.COUNTRY : self.country,
            MongoLocationForecastFields.CITY : self.city,
            MongoLocationForecastFields.TIMEZONE : self.timezone,
            MongoLocationForecastFields.START_FORECAST : self.startForecast,
            MongoLocationForecastFields.END_FORECAST : self.endForecast,
            MongoLocationForecastFields.DAY_HOUR_FORECASTS : dayHourForecastsJsons
        }
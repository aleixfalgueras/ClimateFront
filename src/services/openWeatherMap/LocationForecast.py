from src.commons import MongoLocationForecast


################################################################################
# class: LocationForecast
################################################################################

class LocationForecast :


    ### function: __init__ ###

    def __init__ (self, latitude, longitude, country, city, timezone, forecasts) :
        self.latitude = latitude
        self.longitude = longitude
        self.country = country
        self.city = city
        self.timezone = timezone
        self.forecasts = forecasts

        self.startForecast = forecasts [0].date + " " + forecasts [0].hour
        self.endForecast = forecasts [len (forecasts) - 1].date + " " + forecasts [len (forecasts) - 1].hour


    ### function: toJson ###

    def toJson (self) :
        forecasts = []

        for forecast in self.forecasts : forecasts.append (forecast.toJson ())

        return {
            MongoLocationForecast.LATITUDE : self.latitude,
            MongoLocationForecast.LONGITUDE : self.longitude,
            MongoLocationForecast.COUNTRY : self.country,
            MongoLocationForecast.CITY : self.city,
            MongoLocationForecast.TIMEZONE : self.timezone,
            MongoLocationForecast.START_FORECAST : self.startForecast,
            MongoLocationForecast.END_FORECAST : self.endForecast,
            MongoLocationForecast.FORECAST : forecasts
        }
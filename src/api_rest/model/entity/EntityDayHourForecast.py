from src.commons import MongoDayHourForecast


################################################################################
# class: EntityDayHourForecast
################################################################################

class EntityDayHourForecast :

    ENTITY_NAME = "DayHourForecast"


    ### function: __init__ ###

    def __init__ (self, date, hour, weather, weatherDes, tmp, minTmp, maxTmp, pressure, humidity, windSpeed) :
        self.date = date
        self.hour = hour
        self.weather = weather
        self.weatherDes = weatherDes
        self.tmp = tmp
        self.minTmp = minTmp
        self.maxTmp = maxTmp
        self.pressure = pressure
        self.humidity = humidity
        self.windSpeed = windSpeed


    ### function: toJson ###

    def toJson (self) :
        return {
            MongoDayHourForecast.DATE : self.date,
            MongoDayHourForecast.HOUR : self.hour,
            MongoDayHourForecast.WEATHER : self.weather,
            MongoDayHourForecast.WEATHER_DES : self.weatherDes,
            MongoDayHourForecast.TMP : self.tmp,
            MongoDayHourForecast.TMP_MIN : self.minTmp,
            MongoDayHourForecast.TMP_MAX : self.maxTmp,
            MongoDayHourForecast.PRESSURE : self.pressure,
            MongoDayHourForecast.HUMIDITY : self.humidity,
            MongoDayHourForecast.WIND_SPEED : self.windSpeed
        }
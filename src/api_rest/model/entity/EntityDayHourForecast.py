from src.commons import MongoDayHourForecastFields


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
            MongoDayHourForecastFields.DATE : self.date,
            MongoDayHourForecastFields.HOUR : self.hour,
            MongoDayHourForecastFields.WEATHER : self.weather,
            MongoDayHourForecastFields.WEATHER_DES : self.weatherDes,
            MongoDayHourForecastFields.TMP : self.tmp,
            MongoDayHourForecastFields.TMP_MIN : self.minTmp,
            MongoDayHourForecastFields.TMP_MAX : self.maxTmp,
            MongoDayHourForecastFields.PRESSURE : self.pressure,
            MongoDayHourForecastFields.HUMIDITY : self.humidity,
            MongoDayHourForecastFields.WIND_SPEED : self.windSpeed
        }
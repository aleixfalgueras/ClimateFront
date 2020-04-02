################################################################################
# class: RouteState
################################################################################

class RouteState ():
    PENDING = "PENDING"
    PLANNED = "PLANNED"
    CANCELED = "CANCELED"

################################################################################
# mongo constants
################################################################################

class MongoCollection ():
    PRODUCT = "product"
    ROUTE = "route"

class MongoProductFields:
    ID = "id"
    NAME = "name"
    QUANTITY = "quantity"

class MongoRouteFields:
    ID = "id"
    STATE = "state"
    ORIGIN = "origin"
    DESTINY = "destiny"
    DEPARTURE = "departure"
    ARRIVAL = "arrival"
    PRODUCTS = "products"

class MongoLocationForecast:
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    COUNTRY = "country"
    CITY = "city"
    TIMEZONE = "timezone"
    START_FORECAST = "start_forecast"
    END_FORECAST = "end_forecast"
    FORECAST = "forecasts"

class MongoDayHourForecast:
    DATE = "date"
    HOUR = "hour"
    WEATHER = "weather"
    WEATHER_DES = "weather_description"
    TMP = "temperature"
    TMP_MIN = "temperature_min"
    TMP_MAX = "temperature_max"
    PRESSURE = "pressure"
    HUMIDITY = "humidity"
    WIND_SPEED = "wind_speed"




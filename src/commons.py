################################################################################
# class: RouteState
################################################################################

class RouteState ():
    PENDING = "PENDING"
    PLANNED = "PLANNED"
    CANCELED = "CANCELED"

################################################################################
# class: MongoCollection
################################################################################

class MongoCollection ():
    PRODUCT = "product"
    ROUTE = "route"
    PLAN = "plan"

################################################################################
# class: MongoProductFields
################################################################################

class MongoProductFields:
    ID = "id"
    NAME = "name"
    QUANTITY = "quantity"

################################################################################
# class: MongoRouteFields
################################################################################

class MongoRouteFields:
    ID = "id"
    STATE = "state"
    ORIGIN = "origin"
    DESTINY = "destiny"
    DEPARTURE = "departure"
    ARRIVAL = "arrival"
    PRODUCTS = "products"
    STRATEGY = "strategy"

################################################################################
# class: MongoPlan
################################################################################

class MongoPlan:
    ROUTE = "route"
    STRATEGY = "strategy"
    PLAN = "plan"
    DATE_CREATION = "date_creation"
    HOUR_CREATION = "hour_creation"
    LOCATION_FORECASTS = "location_forecasts"

################################################################################
# class: MongoLocationForecast
################################################################################

class MongoLocationForecast:
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    COUNTRY = "country"
    CITY = "city"
    TIMEZONE = "timezone"
    START_FORECAST = "start_forecast"
    END_FORECAST = "end_forecast"
    DAY_HOUR_FORECASTS = "day_hour_forecasts"

################################################################################
# class: MongoDayHourForecast
################################################################################

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
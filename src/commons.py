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
# class: MongoDayHourForecastFields
################################################################################

class MongoDayHourForecastFields:
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

################################################################################
# class: MongoLocationForecastFields
################################################################################

class MongoLocationForecastFields:
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    COUNTRY = "country"
    CITY = "city"
    TIMEZONE = "timezone"
    START_FORECAST = "start_forecast"
    END_FORECAST = "end_forecast"
    DAY_HOUR_FORECASTS = "day_hour_forecasts"

################################################################################
# class: MongoPlanFields
################################################################################

class MongoPlanFields :
    ROUTE = "route"
    PLAN = "plan"
    LOCATION_FORECASTS = "location_forecasts"
    DATE_CREATION = "date_creation"
    HOUR_CREATION = "hour_creation"
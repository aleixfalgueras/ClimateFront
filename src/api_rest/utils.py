import logging

from src.api_rest.model.entity.EntityDayHourForecast import EntityDayHourForecast
from src.api_rest.model.entity.EntityLocationForecast import EntityLocationForecast
from src.api_rest.model.entity.EntityPlan import EntityPlan
from src.api_rest.model.entity.EntityProduct import EntityProduct
from src.api_rest.model.entity.EntityRoute import EntityRoute
from src.commons import MongoProductFields, MongoRouteFields, MongoDayHourForecastFields, MongoLocationForecastFields, \
    MongoPlanFields

################################################################################
# class: ProdutOperation
################################################################################

class ProdutOperation:
    INCREMENT = "increment"
    DECREMENT = "decrement"

### function: toJsonArray ###

def toJsonArray (entityList):
    try :
        jsonArray = []

        for entity in entityList : jsonArray.append (entity.toJson ())

        return jsonArray

    except Exception as exc :
        logging.error ("utils: toJsonArray: Error getting a JSON array for the entity '" + entityList [0].ENTITY_NAME)
        logging.error ("[Exception: " + str (exc) + "]")


### function: toProducts ###

def toProducts (mongoCursor) :
    try :
        products = []

        for product in mongoCursor :
            products.append (EntityProduct (
                product [MongoProductFields.ID],
                product [MongoProductFields.NAME],
                product [MongoProductFields.QUANTITY]
            ))

        return products

    except Exception as exc :
        logging.error ("utils: toProducts: Error parsing MongoProducts from mongo to " + EntityProduct.ENTITY_NAME)
        logging.error ("[Exception: " + str (exc) + "]")


### function: toRoute ###

def toRoutes (mongoCursor) :
    try:
        routes = []

        for route in mongoCursor :
            routes.append (EntityRoute (
                route [MongoRouteFields.ORIGIN],
                route [MongoRouteFields.DESTINY],
                route [MongoRouteFields.DEPARTURE],
                route [MongoRouteFields.ARRIVAL],
                toProducts (route [MongoRouteFields.PRODUCTS]),
                route [MongoRouteFields.STRATEGY],
                route [MongoRouteFields.ID],
                route [MongoRouteFields.STATE]
            ))

        return routes

    except Exception as exc :
        logging.error ("utils: toRoutes: Error parsing MongoRoutes from mongo to " + EntityRoute.ENTITY_NAME)
        logging.error ("[Exception: " + str (exc) + "]")


### function: toDayHourForecasts ###

def toDayHourForecasts (mongoCursor) :
    try :
        dayHourForecasts = []

        for dayHourForecast in mongoCursor :
            dayHourForecasts.append (EntityDayHourForecast (
                dayHourForecast [MongoDayHourForecastFields.DATE],
                dayHourForecast [MongoDayHourForecastFields.HOUR],
                dayHourForecast [MongoDayHourForecastFields.WEATHER],
                dayHourForecast [MongoDayHourForecastFields.WEATHER_DES],
                dayHourForecast [MongoDayHourForecastFields.TMP],
                dayHourForecast [MongoDayHourForecastFields.TMP_MIN],
                dayHourForecast [MongoDayHourForecastFields.TMP_MAX],
                dayHourForecast [MongoDayHourForecastFields.PRESSURE],
                dayHourForecast [MongoDayHourForecastFields.HUMIDITY],
                dayHourForecast [MongoDayHourForecastFields.WIND_SPEED]
            ))

        return dayHourForecasts

    except Exception as exc :
        logging.error ("utils: toDayHourForecast: Error parsing MongoDayHourForecasts from mongo to " + EntityDayHourForecast.ENTITY_NAME)
        logging.error ("[Exception: " + str (exc) + "]")


### function: toLocationForecasts ###

def toLocationForecasts (mongoCursor) :
    try :
        locationForecasts = []

        for locationForecast in mongoCursor :
            locationForecasts.append (EntityLocationForecast (
                locationForecast [MongoLocationForecastFields.LATITUDE],
                locationForecast [MongoLocationForecastFields.LONGITUDE],
                locationForecast [MongoLocationForecastFields.COUNTRY],
                locationForecast [MongoLocationForecastFields.CITY],
                locationForecast [MongoLocationForecastFields.TIMEZONE],
                toDayHourForecasts (locationForecast [MongoLocationForecastFields.DAY_HOUR_FORECASTS])
            ))

        return locationForecasts

    except Exception as exc :
        logging.error ("utils: toLocationForecasts: Error parsing MongoLocationForecast from mongo to " + EntityLocationForecast.ENTITY_NAME)
        logging.error ("[Exception: " + str (exc) + "]")


### function: toPlans ###

def toPlans (mongoCursor) :
    try :
        plans = []

        for plan in mongoCursor :
            plans.append (EntityPlan (
                toRoutes ([plan [MongoPlanFields.ROUTE]]) [0],
                plan [MongoPlanFields.PLAN],
                toLocationForecasts (plan [MongoPlanFields.LOCATION_FORECASTS]),
                plan [MongoPlanFields.DATE_CREATION],
                plan [MongoPlanFields.HOUR_CREATION]
            ))

        return plans

    except Exception as exc :
        logging.error ("utils: toPlans: Error parsing MongoPlan from mongo to " + EntityPlan.ENTITY_NAME)
        logging.error ("[Exception: " + str (exc) + "]")
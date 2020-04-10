import time
from datetime import datetime

from src.api_rest.model.entity.Entity import Entity
from src.commons import MongoPlanFields


################################################################################
# class: EntityPlan
################################################################################

class EntityPlan (Entity) :

    ENTITY_NAME = "Plan"


    ### function: __init__ ###

    def __init__ (self, route, plan, locationForecasts, id = None, dateCreation = None, hourCreation = None) :
        if id is None :
            self.id = str (time.time_ns ())
        else:
            self.id = id

        if dateCreation is None :
            self.dateCreation = datetime.now ().strftime ("%Y%m%d")
        else:
            self.dateCreation = dateCreation

        if hourCreation is None :
            self.hourCreation = datetime.now ().strftime ("%H%M%S")
        else:
            self.hourCreation = hourCreation

        self.route = route
        self.plan = plan
        self.locationForecasts = locationForecasts


    ### function: toJson ###

    def toJson (self):
        locationForecastsJsons = []

        for locForecast in self.locationForecasts: locationForecastsJsons.append (locForecast.toJson ())

        return {
            MongoPlanFields.ID : self.id,
            MongoPlanFields.ROUTE : self.route.toJson (),
            MongoPlanFields.PLAN : self.plan,
            MongoPlanFields.LOCATION_FORECASTS : locationForecastsJsons,
            MongoPlanFields.DATE_CREATION : self.dateCreation,
            MongoPlanFields.HOUR_CREATION : self.hourCreation
        }
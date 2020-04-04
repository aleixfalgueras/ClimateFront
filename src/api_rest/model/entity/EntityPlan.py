from datetime import datetime

from src.commons import MongoPlanFields


################################################################################
# class: EntityPlan
################################################################################

class EntityPlan:

    ENTITY_NAME = "Plan"


    ### function: __init__ ###

    def __init__ (self,
                  route,
                  plan,
                  locationForecasts,
                  dateCreation = datetime.now ().strftime ("%Y%m%d"),
                  hourCreation = datetime.now ().strftime ("%H%M%S")) :
        self.route = route
        self.plan = plan
        self.locationForecasts = locationForecasts
        self.dateCreation = dateCreation
        self.hourCreation = hourCreation


    ### function: toJson ###

    def toJson (self):
        locationForecastsJsons = []

        for locForecast in self.locationForecasts: locationForecastsJsons.append (locForecast.toJson ())

        return {
            MongoPlanFields.ROUTE : self.route.toJson (),
            MongoPlanFields.PLAN : self.plan,
            MongoPlanFields.LOCATION_FORECASTS : locationForecastsJsons,
            MongoPlanFields.DATE_CREATION : self.dateCreation,
            MongoPlanFields.HOUR_CREATION : self.hourCreation
        }
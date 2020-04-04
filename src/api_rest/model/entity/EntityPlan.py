from datetime import datetime

from src.commons import MongoPlan


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
            MongoPlan.ROUTE : self.route.toJson (),
            MongoPlan.PLAN : self.plan,
            MongoPlan.LOCATION_FORECASTS : locationForecastsJsons,
            MongoPlan.DATE_CREATION : self.dateCreation,
            MongoPlan.HOUR_CREATION : self.hourCreation
        }
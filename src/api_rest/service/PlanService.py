import logging

from src.api_rest.utils import toPlans
from src.commons import MongoCollection
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton


### function: getPlans ###

def getPlans (filters = None) :
    try :
        query = {}
        if filters is not None : query = filters

        logging.info ("PlansService: getPlans: filters: [" + str (filters) + "]")

        res = MongoClientSingleton ().getCollection (MongoCollection.PLAN).find (query)

        return toPlans (res)

    except Exception as exc :
        logging.error ("PlanService: getPlans: Error getting plans, filters: " + str (filters))
        logging.error ("[Exception: " + str (exc) + "]")


### function: addPlan ###

def addPlan (route):
    try :
        plan = route.strategy.planIt (route)

        MongoClientSingleton ().getCollection (MongoCollection.PLAN).insertOne (plan.toJson ())

        return plan

    except Exception as exc :
        logging.error ("PlanService: addPlan: Error creating plan for the route: " + str (route))
        logging.error ("[Exception: " + str (exc) + "]")
### function: toJsonArray ###

def toJsonArray (entityList):
    jsonArray = []

    for entity in entityList: jsonArray.append (entity.toJson ())

    return jsonArray
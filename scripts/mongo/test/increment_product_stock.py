db.getCollection('product').updateOne({"id" : "2"}, {"$set" : {"quantity" : "10"}});
db.getCollection('product').updateOne({"id" : "3"}, {"$set" : {"quantity" : "10"}});
db.getCollection('product').updateOne({"id" : "4"}, {"$set" : {"quantity" : "10"}});
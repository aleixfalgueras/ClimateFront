db.route.createIndex ({id: -1});
db.route.createIndex ({state: -1});
db.route.createIndex ({origin: -1});
db.route.createIndex ({destiny: -1});
db.route.createIndex ({departure: -1});
db.route.createIndex ({arrival: -1});

db.route.createIndex ({origin: -1, destiny: -1});
db.route.createIndex ({departure: -1, arrival: -1});
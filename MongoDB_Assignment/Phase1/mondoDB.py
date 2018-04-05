import pymongo
from pymongo import MongoClient
from bson import json_util
client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
Airports = db.airport
print(Airports)
with open("airport.json","r") as f:
    data = json_util.loads(f.read())
# print(data)
# insert this data to mongo db dataset.
res = Airports.insert_many(data)

#Lets do some printing and test out the results
#sort the countries by their name Z --> A
country_sort = Airports.find().sort([("country", pymongo.DESCENDING),])
for countries in country_sort:
    print(countries["country"])

# Lets dig more 
state = Airports.find({"country": "India"})
for states in state:
    print("Name: {}. City: {}. State: {}. ".format(states["name"], states["city"], states["state"]))

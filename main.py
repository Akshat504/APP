'''
  Author: Akshat Saini
'''

from pymongo import MongoClient


# client = MongoClient()
client = MongoClient('localhost')

# # db = client.test_database         # name of the database

db = client['test-database']            # name of the database in dictionary style 



# # collection = db.test_collection    # name of the collection in test_database

collection = db['test-collection']      # name of the collection in dictionary style 



#  C- Create Operation or Insert the data


# mydict = {"name": "Peter", "address": "Lowstreet 27"}

# insert the one id data in collection

# x = collection.insert_one(mydict).inserted_id
# print(x)

#  Read Operation or getting the collection data


# a =collection.find_one()      
# print(a)


# Insert the multiple data with default ids

# mylist = [
#     {"name": "Amy", "address": "Apple st 652"},
#     {"name": "Hannah", "address": "Mountain 21"},
#     {"name": "Michael", "address": "Valley 345"},
#     {"name": "Sandy", "address": "Ocean blvd 2"},
#     {"name": "Betty", "address": "Green Grass 1"},
#     {"name": "Richard", "address": "Sky st 331"},
#     {"name": "Susan", "address": "One way 98"},
#     {"name": "Vicky", "address": "Yellow Garden 2"},
#     {"name": "Ben", "address": "Park Lane 38"},
#     {"name": "William", "address": "Central st 954"},
#     {"name": "Chuck", "address": "Main Road 989"},
#     {"name": "Viola", "address": "Sideway 1633"}
# ]

# y = collection.insert_many(mylist).inserted_ids
# print(y)


#  Read Operation or getting the collection data

# for b in collection.find():
#         print(b)


# Insert Multiple Documents, with Specified IDs

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

# z = collection.insert_many(mylist).inserted_ids
# print(z)

#  Read Operation or getting the collection data

# for c in collection.find():
#         print(c)
myquery = { 'name': 'William' }
for c in collection.find_one(myquery):
  print(c)
# with this find method, if we put key = 0, then which key has 0 value will not print, remaining print


# for x in collection.find({},{ "_id": 0, "name": 1, "address": 1 }):       # print the name and address without id
#         print(x)


# for y in collection.find({},{ "address": 0 }):      # print the id and names without address
#         print(y)


# Update Operation


#  update the one data and change the address valley to canyon


# myquery = { "address": "Valley 345" }                                 # old entry
# newvalues = { "$set": { "address": "Canyon 123" } }                   # new entry

# collection.update_one(myquery, newvalues)
# for f in collection.find():
#         print(f)


#  update "Minnie" name where the address start with the letter S


# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }

# h = collection.update_many(myquery, newvalues)

# print(h.modified_count, "documents updated.")        # modified count, count the how many updates happen in collection data

# for h in collection.find():
#         print(h)


# Delete Operation



# myquery = { "address": "Mountain 21" }                          # delete the complete row where address = mountain 21

# i = collection.delete_one(myquery)                              # delete one data
# for i in collection.find():
#         print(i)




# myquery = { "address": {"$regex": "^O"} }

# k = collection.delete_many(myquery)

# print(k.deleted_count, " documents deleted.")
# for k in collection.find():
#         print(k)


#  find the data which is mention in collection

# myquery = { "address": "Park Lane 38" }

# mydoc = collection.find(myquery)

# for t in mydoc:
#   print(t)

#  find the data which is greater than S alphabet

# myquery = { "address": { "$gt": "S"} }

# mydoc = collection.find(myquery)

# for s in mydoc:
#   print(s)


#  Limit the result to only return 5 documents:

# myresult = collection.find().limit(5)

# for g in myresult:
#   print(g)


#  for drop the collection

# r = collection.drop()
# print(r,"Collection drop successfully!")
